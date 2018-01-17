#! /usr/bin/python
#
# HOW TO USE: 
#
# HAVE TO RUN THIS SCRIPT WITH SUDO PRIVILIDGES. Shutdown commands needs SUDO.
# If you plan to run this from a cron job, you can exit the utility if the battery is
# good. This sample shows how the command is run in a loop. 
# Command usage:
# sudo python <filename.py>
# where file name is the name for this file.
#
#
# RIGHT TO USE STATEMENT
# (C) 2017 Alchemy Power Inc.
# Right to use, copy, distribute etc. of this code with Pi-UpTimeUPS or
# PiZ-UpTime or any other Alchemy Power Inc. product or any product. Right is granted to you
# by Alchemy Power Inc. as long as you maintain the lines from line 1 to "END OF HEADERS" line
# with every copy.
#
####################  END OF HEADERS  ##########################
#
#
# This file shows alternate ways to use the Python code. You can use whichever one you
# are familair with.
#
# Instead of firt line /usr/bin/python, you can use line below to setup the environment for Python.
#
#!/usr/bin/env python
#
#
#
import RPi.GPIO as GPIO
import time
#
# import os if using the os method to initiate the shutdown.
#
import os
#
# sys is needed for flushing std out on an interrupt.
#
import sys
#
# import subprocess to start the shut down process as a seperate thread
# and exit the script cleaning out the GPIO. 
#
import subprocess
# Use the number carefully - GPIO.BOARD for pin number on the board.
# Use the BCM method if 
# Use the GPIO.BCM if you are using the BCM method to assign the GPIO number.
# Make sure the GPIO jumper is in.
# If the GPIO jumper is out, the GPIO connection is broken.
#
buttonPin = 37 # GPIO 26, Pin 37
# Use pin number 37 on the board by using the setmode below.
#
GPIO.setmode(GPIO.BOARD)
#
# Use GPIO number if you are using BCM technique below.
# GPIO.setmode(GPIO.BCM)
#
# Use the pull up i.e. expect output to be zero. When it goes to 1, GPIO is set.
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
# Opposite of what we did above - normally 1, GPIO set when it goes to zero.
# GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#
# Use schlaf variable below to indicate how long the program sleeps for before checking again.
#
schlaf = 10
while True:
	if (GPIO.input(buttonPin)):
		# GPIO is 0
		# Debug
		# print("GPIO is 0 ")
		# This just prints the time letting you know if the Pi is up. This can be logged
		# to keep track of pi. Note comment line if you are using the cron method to check battery 
		# status.
		print("Time is %s " % (time.ctime()))
		# os.system('echo yea-yea')
		time.sleep(schlaf)
	else:
		# GPIO is 1. We are here because the sensors triggered the battery being low.
		print("Shutdown initiated at %s " % (time.ctime()))
		#
		# The command shuts down the pi in 2 minutes. Replace
		# 2 with word "now" (without the quotes) for immediate
		# shutdown. If you use the Pi-Zero-Uptime (the one which uses 14500 battery)
		# recommend using shutdown -h now instead of shutdown -h 2.
		# The subprocess method forks a process which can run in the background while this
		# program exits properly. os.system method continues to run in the program thread.
		#
		# os.system('sudo shutdown -h 2')
		#
		subprocess.call("shutdown -h 2 &", shell=True)
		#
		# Sleep for a second or so for the shutdown process to fork and then exit
		# script cleaning out GPIO.
		time.sleep(2)
		# Flush any stdout messages before exiting..
		sys.stdout.flush()
		# exit the while monitoring loop.
		exit()
	# Flush any buffers if ^C or interrupt is pressed.
	sys.stdout.flush()
# Clean up GPIO handler on exit of the script.
# Clean up is optional. If the system reboots it will clean up!
# GPIO.cleanup()
