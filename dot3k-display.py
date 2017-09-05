#!/usr/bin/env python

import time, colorsys, psutil, subprocess
import dot3k.lcd as lcd
import dot3k.backlight as backlight
from dot3k.menu import Menu, MenuOption

def run_cmd(cmd):
	p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output = p.communicate()[0].rstrip()
	return output

def millis():
	return int(round(time.time() * 1000.0))

def lcd_colour(percent):
	f = float(percent) / 100
	# there's a good colour change between these hues on a dot3k *RBG* display:
	start = 270
	end = 330
	step = end - start
	hue = (start + (f * step)) / 360
	backlight.hue(hue)

def bytes2human(n):
	# http://code.activestate.com/recipes/578019
	symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
	prefix = {}
	for i, s in enumerate(symbols):
		prefix[s] = 1 << (i + 1) * 10
	for s in reversed(symbols):
		if n >= prefix[s]:
			value = float(n) / prefix[s]
			return '%.0f%s' % (value, s)
			return "%sB" % n

class cpu_info(MenuOption):
	
	def begin(self):
		self.load_average_5m = run_cmd("uptime | grep -ohe 'load average[s:][: ].*' | awk '{ print $4 }'| tr -d ','")
	
	def get_cpu_temp(self):
		tempFile = open("/sys/class/thermal/thermal_zone0/temp")
		cpu_temp = tempFile.read()
		tempFile.close()
		return int(cpu_temp) / 1000
		
	def redraw(self,menu):
		cpu_percent = psutil.cpu_percent(interval=0)
		cpu_temp = self.get_cpu_temp()
		
		lcd_colour(cpu_percent)
		menu.write_row(0,'-= CPU =-')
		menu.write_row(1,'Load: %.0f%% (%s)' % (cpu_percent, self.load_average_5m))
		menu.write_row(2,'Temp: %s C' % str(cpu_temp))

class memory_info(MenuOption):
	
	def redraw(self,menu):
		available_memory = bytes2human(psutil.virtual_memory().available)
		active_memory = bytes2human(psutil.virtual_memory().active)
		percent_used = psutil.virtual_memory().percent
		percent_free = 100 - percent_used
		
		lcd_colour(percent_used)
		menu.write_row(0,'-= RAM =-')
		menu.write_row(1,'Used: %s (%.0f%%)' % (active_memory, percent_used))
		menu.write_row(2,'Free: %s (%.0f%%)' % (available_memory, percent_free))

class disk_info(MenuOption):
	
	def redraw(self,menu):
		percent_used_root = psutil.disk_usage('/').percent
		percent_used_usb = psutil.disk_usage('/mnt/SandiskUSB').percent
		
		lcd_colour(percent_used_root)
		menu.write_row(0,'-= HDD =-')
		menu.write_row(1,'Used (/):   %.0f%%' % percent_used_root)
		menu.write_row(2,'Used (USB): %.0f%%' % percent_used_usb)

class network_info(MenuOption):
	
	def __init__(self,interface):
		self.interface = interface
		MenuOption.__init__(self)
	
	def begin(self):
		self.ip_address = run_cmd("ifconfig " + self.interface + " | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'")
		self.ping = run_cmd("ping -c 1 -I " + self.interface + " 8.8.8.8 | grep time= | awk '{ print $7 }' | cut -d'=' -f2")
		
		if not self.ip_address:
			self.ip_address = 'No IP address!' 
		
		try:
			self.ping = float(self.ping)
		except:
			pass
		
		# define screen colours based on ping values, arbitrarily: 0-20=good, 20-40=ok, 40-100=hmm, >100=crap
		if 0 <= self.ping < 20:
			self.colour = 0
		elif 20 <= self.ping < 40:
			self.colour = 25
		elif 40 <= self.ping < 100:
			self.colour = 50
		elif self.ping <= 100:
			self.colour = 75
		else:
			self.colour = 100		# unreachable
			self.ping = ';-(      '	# padd the 'ms' off the screen
			
		#self.connections = run_cmd("netstat -tun | grep -c ESTABLISHED")
		#self.mac_address = run_cmd("ifconfig " + self.interface + " | grep HWaddr | awk '{ print $5 }' | sed s/://g") 
		
	def redraw(self,menu):
		lcd_colour(self.colour)
		menu.write_row(0,'-= ' + self.interface + ' =-')
		menu.write_row(1,'%s' % self.ip_address) # xxx.xxx.xxx.xxx = 15 chars max
		menu.write_row(2,'Ping: %s ms' % self.ping)
		#menu.write_row(2,'%s' % self.mac_address) # xx:xx:xx:xx:xx:xx (17 chars, have to remove ':')
		#menu.write_row(2,'%s connections' % self.connections)

class network_speed(MenuOption):
	
	def __init__(self,interface):
		self.last_updated = 0
		self.raw_dlold = 0
		self.raw_ulold = 0
		self.tdelta = 0
		self.maxdlspeed = 1000
		self.percent_speed = 0
		self.interface = interface
		MenuOption.__init__(self)
		
	def begin(self):
		self.download = bytes2human(int(run_cmd("ifconfig " + self.interface + " | grep bytes | awk '{ print $2 }' | cut -d':' -f2")))
		self.upload = bytes2human(int(run_cmd("ifconfig " + self.interface + " | grep bytes | awk '{ print $6 }' | cut -d':' -f2")))
		
	def redraw(self,menu):
		
		if self.millis() - self.last_updated > 1000:
			tdelta = self.millis() - self.last_updated
			self.last_updated = self.millis()
			raw_dlnew = run_cmd("ifconfig " + self.interface + " | grep bytes | cut -d':' -f2 | cut -d' ' -f1")
			raw_ulnew = run_cmd("ifconfig " + self.interface + " | grep bytes | cut -d':' -f3 | cut -d' ' -f1")
			self.dlspeed = 0
			self.ulspeed = 0
			try:
				ddelta = int(raw_dlnew) - int(self.raw_dlold)
				udelta = int(raw_ulnew) - int(self.raw_ulold)
				self.dlspeed = round(float(ddelta) / float(tdelta), 1)
				self.ulspeed = round(float(udelta) / float(tdelta), 1)
			except ValueError:
				pass
			
			if self.dlspeed > self.maxdlspeed:
				self.maxdlspeed = self.dlspeed
			
			self.percent_speed = self.dlspeed / self.maxdlspeed * 100
			#print "speed %s / %s (%s)" % (self.dlspeed,self.maxdlspeed,self.percent_speed)
			self.raw_dlold = raw_dlnew
			self.raw_ulold = raw_ulnew
		
		lcd_colour(self.percent_speed)
		menu.write_row(0,'-= ' + self.interface + ' =-')
		menu.write_row(1,'Dn:%s %skB/s' % (self.download,self.dlspeed))
		menu.write_row(2,'Up:%s %skB/s' % (self.upload,self.ulspeed))

#class sample_info(MenuOption):
#	
#	def begin(self):
#		self.slowvar = run_cmd("") # runs once per menu change, for slowly updating info
#		
#	def redraw(self,menu):
#	
#		self.fastvar = run_cmd("") # updated every screen refresh, for rapidly changing data
#	
#		lcd_colour(0)	# displays warning colour background, set this to a range 0..100, 0 = green, 100 = red
#		menu.write_row(0,'-= AFP =-')
#		menu.write_row(1,'slow: %s' % self.slowvar)
#		menu.write_row(2,'fast: %s' % self.fastvar)

menu = Menu({
		'1': cpu_info(),
		'2': memory_info(),
		'3': disk_info(),
		'4': network_info('wlan0'),
		'5': network_speed('wlan0'),
		'6': network_info('eth0'),
		'7': network_speed('eth0'),
		},
	lcd, None, 30)

menu_display_time = 4	# in seconds
update_frequency = 5	# hz of screen update
last_cycled = 0			# force immediate update of screen menu

#try:
while True:
	if millis() > last_cycled + (menu_display_time * 1000.0):
		menu.cancel()
		menu.down()
		menu.right()
		last_cycled = millis()
	else:
		menu.redraw()
	time.sleep(1 / float(update_frequency))
#except:
#	lcd.clear()
#	backlight.rgb(0,0,0)
