#!/usr/bin/python
# --------------------------------------------------------------------------
# Script executed by systemd service for gpio-poll.service.
#
# Please edit /etc/gpio-poll.conf to configure the GPIOs to monitor
# and the scripts to be started.
#
# Author: Bernhard Bablok
# License: GPL3
#
# Website: https://github.com/bablokb/gpio-poll-service
#
# --------------------------------------------------------------------------

import select, os, sys, syslog, signal, time
import ConfigParser

FIFO_NAME="/var/run/gpio-poll.fifo"

# --- helper functions   ---------------------------------------------------

""" write a value to the given path """

def set_value(path, value):
  fd = open(path, 'w')
  fd.write(value)
  fd.close()
  return

# --------------------------------------------------------------------------

def write_log(msg):
  global debug
  if debug == '1':
    syslog.syslog(msg)

# --------------------------------------------------------------------------

""" return global configurations (debug, array of configured GPIOs) """

def get_global(cparser):
  # read debug first, so that get_value can write to log
  global debug
  debug = get_value(cparser,'GLOBAL','debug','0')
  gpios = cparser.get('GLOBAL','gpios')

  global_conf = {
    # global constants
    'debug':      debug,
    'fifo' :      get_value(cparser,'GLOBAL','fifo','0'),

    # defaults for gpio-sections
    'command':     get_value(cparser,'GLOBAL','command',None),
    'edge':        get_value(cparser,'GLOBAL','edge','both'),
    'act_low':     get_value(cparser,'GLOBAL','active_low','0'),
    'ig_init':     get_value(cparser,'GLOBAL','ignore_initial','0'),
    'bounce_time': get_value(cparser,'GLOBAL','bounce_time','0'),

    # list of gpios
    'gpios':      [entry.strip() for entry in gpios.split(',')]
  }
  return global_conf

# --------------------------------------------------------------------------

""" get value of config-variable and return given default if unset """

def get_value(cparser,section,option,default):
  if cparser.has_section(section):
    try:
      value = cparser.get(section,option)
    except:
      write_log("option %s not in [%s]. Using default: %s" % (option,section,default))
      value = default
  else:
      write_log("no section [%s]. Using default for %s: %s" % (section,option,default))
      value = default
  return value

# --------------------------------------------------------------------------

""" parse configuration """

def get_config(cparser,global_conf):
  gpios = global_conf['gpios']
  info = {}
  now = time.time()
  for gpio in gpios:
    section   = 'GPIO'+gpio
    command   = get_value(cparser,section,'command',global_conf['command'])
    edge      = get_value(cparser,section,'edge',global_conf['edge'])
    act_low   = get_value(cparser,section,'active_low',
                          global_conf['act_low'])
    ig_init   = get_value(cparser,section,'ignore_initial',
                          global_conf['ig_init'])
    bounce_time = get_value(cparser,section,'bounce_time',
                            global_conf['bounce_time'])

    info[gpio] = {'command':     command,
                  'edge':        edge,
                  'ig_init':     ig_init,
                  'act_low':     act_low,
                  'bounce_time': bounce_time,
                  '0':         now,             # timestamp value 0
                  '1':         now}             # timestamp value 1
  return info

# --------------------------------------------------------------------------

""" configure GPIOs """

def setup_pins(info):
  gpio_root = '/sys/class/gpio/'
  for num, entry in info.iteritems():
    edge = entry['edge']
    act_low = entry['act_low']
    gpio_dir  = gpio_root + 'gpio'+num+'/'
    if not os.path.isdir(gpio_dir):
      set_value(gpio_root + 'export', num)
    set_value(gpio_dir  + 'direction', 'in')
    set_value(gpio_dir  + 'edge', edge)
    set_value(gpio_dir  + 'active_low', act_low)

# --------------------------------------------------------------------------

""" setup poll-object and register file-descriptors """

def setup_poll(info):
  poll_obj = select.poll()
  fdmap = {}
  for num in info:
    gpio_dir  = '/sys/class/gpio/gpio'+num+'/'
    fd  = open(gpio_dir + 'value', 'r')
    fno = fd.fileno()
    # read and discard state in case ignore_initial is set
    if info[num]['ig_init'] == '1':
      write_log("ignoring initial value for %s" % num)
      fd.seek(0)
      fd.read(1)
    fdmap[fno] = { 'num': num, 'fd': fd }   # keep ref to fd to prevent
    poll_obj.register(fd,select.POLLPRI)    # garbage collection
  return poll_obj, fdmap

# --------------------------------------------------------------------------

""" signal-handler to cleanup GPIOs """

def signal_handler(_signo, _stack_frame):
  write_log("interrupt %d detected, exiting" % _signo)
  global info, fifo
  gpio_root = '/sys/class/gpio/'
  for num, entry in info.iteritems():
    set_value(gpio_root + 'unexport', num)
  if global_conf['fifo'] != '0':
    fifo.close()
  sys.exit(0)

# --- main program   ------------------------------------------------------

debug='0'
syslog.openlog("gpio-poll")
parser = ConfigParser.RawConfigParser()

# read configuration
parser.read('/etc/gpio-poll.conf')
global_conf = get_global(parser)        # also sets debug
info = get_config(parser,global_conf)

# dump configuration to system log
write_log("Global-config: " + str(global_conf))
gpios = global_conf['gpios']
write_log("GPIOs: " + str(gpios))
write_log("GPIO-config: " + str(info))

# setup signal handlers and pins
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)
setup_pins(info)

# setup poll
poll_obj, fdmap = setup_poll(info)

# setup fifo
if global_conf['fifo'] != '0':
  write_log("creating fifo %s" % FIFO_NAME)
  if os.path.exists(FIFO_NAME):
    os.unlink(FIFO_NAME)
  os.mkfifo(FIFO_NAME,0644)
  fifo = open(FIFO_NAME,"rw+",0)

# --- main loop   ---------------------------------------------------------

while True:
  # wait for interrupt
  poll_result = poll_obj.poll()
  ts_current = time.time()

  # read values
  for (fd,event) in poll_result:
    write_log("processing fd %s (event: %d)" % (fd,event))

    # do some sanity checks
    if event & select.POLLIN == select.POLLIN:
      write_log("event POLLIN not expected. Reading anyhow")
    elif event & select.POLLPRI != select.POLLPRI:
      write_log("event not POLLIN/POLLPRI. Ignoring event")
      continue

    # read current state of GPIO
    os.lseek(fd,0,os.SEEK_SET)
    state = int(os.read(fd,1))

    # get gpio-number from filename
    num = fdmap[fd]['num']
    write_log("state[%s]: %d" % (num,state))
    gpio_info = info[num]

    # check for invalid value (this does happen)
    if gpio_info['edge'] == 'rising':
      if state == 0:
        write_log("invalid state %d for edge==rising. Ignoring" % state)
        continue
    elif gpio_info['edge'] == 'falling':
      if state == 1:
        write_log("invalid state %d for edge==falling. Ignoring" % state)
        continue

    # calculate intervals ...
    int_repeat = ts_current - gpio_info[str(state)]
    if gpio_info['edge'] == 'both':
      int_switch = ts_current - gpio_info[str(1-state)]
    else:
      int_switch = -1

    # check for bouncing
    bounce_limit = float(gpio_info['bounce_time'])
    if  bounce_limit > 0.0:
      if int_repeat < bounce_limit:
        write_log("ignoring event (repeat-time %g less than bounce_time %g)"
                  % (int_repeat,bounce_limit))
        continue

    # ...and update current timestamp
    gpio_info[str(state)] = ts_current


    # in fifo-mode, write to fifo
    if global_conf['fifo'] != '0':
      write_log("writing event to fifo")
      fifo.write("%s %d %g %g\n" % (num,state,int_switch,int_repeat))
    else:
      # execute command
      command = gpio_info['command']
      if command:
        write_log("executing %s" % command)
        os.system("%s %s %d %g %g &" % (command,num,state,int_switch,int_repeat))
      else:
        write_log("command not defined, ignoring event")
