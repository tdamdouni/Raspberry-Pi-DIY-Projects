import RPi.GPIO as GPIO
from time import sleep
from ISStreamer.Streamer import Streamer

# Tell the Pi we're going to use it's numbering system
GPIO.setmode(GPIO.BCM)
# Pin that D1 is connected to
PIN=23

# Specify our pin as input
GPIO.setup(PIN,GPIO.IN)

# Initial State bucket name (displayed)
BUCKET_NAME = ":wave: Motion Sensor" 
# Initial State bucket key (hidden)
BUCKET_KEY = "pizerowmotion"
# Initial State access key
ACCESS_KEY = "Your_Access_Key_Here"

# Variables that ensure we don't stream "Motion Detected" or "No Motion" twice in a row
# This saves on sent events and processing power
alreadyRecordedMotion = False
alreadyRecordedNoMotion = False

# Initialize the Initial State Streamer
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

# Loop indefinitely
while True:
	# If the motion sensor pulls high (detects motion):
	if GPIO.input(PIN) == 1:
		print "Motion detected"
		# If we haven't streamed yet:
		if not alreadyRecordedMotion:
			# Stream to Initial State
			streamer.log(":spy: Anybody Around?",":runner: Motion Detected")
			streamer.flush()
			alreadyRecordedMotion = True
			alreadyRecordedNoMotion = False
		else:
			# Pause the script for 1 second
			sleep(1)
	else:
		print "No motion detected"
		# If we haven't streamed yet:
		if not alreadyRecordedNoMotion:
			# Stream to Initial State
			streamer.log(":spy: Anybody Around?",":no_pedestrians: No Motion")
			streamer.flush()
			alreadyRecordedNoMotion = True
			alreadyRecordedMotion = False
		else:
			# Pause the script for 1 second
			sleep(1)
