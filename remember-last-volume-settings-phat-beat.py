#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://raw.githubusercontent.com/snakewa/phat-beat/063ae1952204ea14a6af32dc913a39ff9daeb937/projects/vlc-radio/phatbeatd/usr/bin/phatbeatd

# http://forums.pimoroni.com/t/pi-zero-w-pirate-radio-and-the-phatbeat/4099/67

from threading import Timer
import atexit
import re
import socket
import subprocess
import time
import os
import signal
import sys
import json
import io
from datetime import datetime

VLC_HOST = "127.0.0.1"
VLC_PORT = 9294

LOG_LEVEL = 0

PIDFILE = "/var/run/phatbeatd.pid"
STATEFILE = "/home/pi/phatbeatd.json"
LOGFILE = "/var/log/phatbeatd.log"
ERRFILE = "/var/log/phatbeatd.err"

SHUTDOWN_HOLD_TIME = 3

LOG_INFO = 0
LOG_WARN = 1
LOG_FAIL = 2
LOG_DEBUG = 3

phatbeatd_state={}
def read_state():
  global phatbeatd_state
  try:
      with open(STATEFILE) as data_file:
        phatbeatd_state = json.load(data_file)
  except:
      phatbeatd_state = {}

def write_state(key,value):
    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str
    phatbeatd_state[key]=value
    with io.open(STATEFILE, 'w', encoding='utf8') as outfile:
      str_ = json.dumps(phatbeatd_state,
                        indent=4, sort_keys=True,
                        separators=(',', ':'), ensure_ascii=False)
      outfile.write(to_unicode(str_))

def log(msg, level=LOG_INFO):
    if level < LOG_LEVEL: return

    sys.stdout.write(str(datetime.now()))
    sys.stdout.write(": ")
    sys.stdout.write(msg)
    sys.stdout.write("\n")
    sys.stdout.flush()

class VLC():

    def __init__(self, host="127.0.0.1", port=9294):
        self.host = host
        self.port = port
        self.current_stream = None
        self.current_state = None
        self.connecting = False
        self.socket = None

    def send(self, command):
        if self.connecting:
            return False

        log("Sending command: {}".format(command), level=LOG_INFO)
        command_string = command + "\n"

        if sys.version_info[0] >= 3:
            command_string = command_string.encode("utf-8")

        try:
            self.socket.send(command_string)

        except socket.error:
            log("Failed to send command to VLC", level=LOG_WARN) 
            if self.connect():
                self.send(command)

    def recv(self, length):
        value = self.socket.recv(8192)

        if sys.version_info[0] >= 3:
            value = value.decode("utf-8")

        return value

    def communicate(self, command, response_length=8192):
        self.send(command)
        return self.recv(response_length)

    def get_current_stream(self):
        self.send("status")
        status = self.recv(8192)

        result = re.search("input:\ (.*)\ ", status)
        state = re.search("state\ (.*)\ ", status)

        if state is not None:
            self.current_state = state.group(1)

        if result is not None:
            self.current_stream = result.group(1)
        else:
            self.current_stream = None

        return self.current_stream

    def connect(self):
        if self.connecting:
            return

        self.connecting = True

        if self.socket is not None:
            self.socket.close()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        for attempt in range(10):
            try:
                log("Attempting to connect to VLC on {host}:{port}".format(host=self.host, port=self.port))
                self.socket.connect((self.host, self.port))
                log("Connection successful!", level=LOG_INFO)
                self.connecting = False
                return True

            except socket.error:
                time.sleep(1)

        log("Connection failed!", level=LOG_FAIL)
        self.connecting = False
        return False


if __name__ == "__main__":
    stdin = None
    stdout = None
    stderr = None
    fpid = None
    daemonize = True
    pid = None

    def _signal_handler(signal, frame):
        _cleanup()
        sys.exit(0)

    def _cleanup():
        log("Exiting cleanly")

        try:
            os.remove(PIDFILE)
        except OSError:
            pass

        if stdin is not None: stdin.close()
        if stdout is not None: stdout.close()
        if stderr is not None: stderr.close()

    if daemonize:
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)

        except OSError, e:
            log("Fork #1 failed: {} ({})".format(e.errno, e.strerror))
            sys.exit(1)

        os.chdir("/")
        os.setsid()
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)

        except OSError, e:
            log("Fork #2 failed: {} ({})".format(e.errno, e.strerror))
            sys.exit(1)

    pid = os.getpid()
    fpid = open(PIDFILE, 'w')
    fpid.write(str(pid))
    fpid.close()

    log("PHAT BEAT {} running with PID: {}".format("daemon" if daemonize else "process",pid))

    stdin = file("/dev/null", 'r')
    stdout = file(LOGFILE, 'a+')
    stderr = file(ERRFILE, 'a+')

    os.dup2(stdin.fileno(), sys.stdin.fileno())
    os.dup2(stdout.fileno(), sys.stdout.fileno())
    os.dup2(stderr.fileno(), sys.stderr.fileno())

    vlc = VLC(host=VLC_HOST, port=VLC_PORT)

    if vlc.connect():
        import phatbeat
        phatbeat.set_all(0,128,0,0.1)
        phatbeat.show()
        time.sleep(1)
        phatbeat.clear()
        phatbeat.show()

        read_state()
        #init vol
        if 'volume' in phatbeatd_state:
            log('set init volume: %d' % phatbeatd_state['volume'])
            log(vlc.communicate( "volume %d" % phatbeatd_state['volume']))

        def store_volume(cmd_response):
            vol = [int(s) for s in cmd_response.split() if s.isdigit()]
            if len(vol) >=1 :
                write_state('volume', vol[0])
            return cmd_response

        @phatbeat.on(phatbeat.BTN_VOLDN)
        def pb_volume_down(pin):
            log(store_volume(vlc.communicate("voldown")))
            
        @phatbeat.on(phatbeat.BTN_VOLUP)
        def pb_volume_up(pin):
            log(store_volume(vlc.communicate("volup")))

        @phatbeat.on(phatbeat.BTN_PLAYPAUSE)
        def pb_play_pause(pin):
            log(vlc.communicate("pause"))
            time.sleep(0.1)
            phatbeat.clear()
            phatbeat.show()

        @phatbeat.on(phatbeat.BTN_FASTFWD)
        def pb_fast_forward(pin):
            log(vlc.communicate("next"))

        @phatbeat.on(phatbeat.BTN_REWIND)
        def pb_rewind(pin):
            log(vlc.communicate("prev"))

        @phatbeat.on(phatbeat.BTN_ONOFF)
        def perform_shutdown(pin):
            log(vlc.communicate("pause"))
            os.system("sudo shutdown -h now")

        signal.signal(signal.SIGINT, _signal_handler)
        signal.signal(signal.SIGTERM, _signal_handler)
        signal.pause()

        _cleanup()
        sys.exit(0)

    else:
        _cleanup()
        sys.exit(1)