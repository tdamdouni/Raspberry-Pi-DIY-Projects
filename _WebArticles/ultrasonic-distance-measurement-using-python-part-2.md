# Ultrasonic Distance Measurement Using Python – Part 2

_Captured: 2017-09-09 at 16:46 from [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2013/01/ultrasonic-distance-measurement-using-python-part-2/)_

![Ultrasonic Sensor](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/12/Ultrasonic-Sensor-03-702x336.jpg)

Following on from my [Ultrasonic Distance Measurement Using Python - Part 1](https://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/) article I decided to make my Python script a little bit more sophisticated.

In this example the script takes three measurements and calculates the average. This is displayed and one second later it takes another average. This allows the script to be used to constantly measure distances and print them to the command line.

The Ultrasonic module is connected as before to the Raspberry Pi using a small piece of breadboard and some jumper cables.

The Trigger accepts a 3.3V output from the Pi but the Echo pin must be converted to 3.3V from 5V before it reaches the GPIO input.

## Python Script

Here is the modified script :
    
    
    #!/usr/bin/python
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #
    # ultrasonic_2.py
    # Measure distance using an ultrasonic module
    # in a loop.
    #
    # Author : Matt Hawkins
    # Date   : 28/01/2013
    
    # -----------------------
    # Import required Python libraries
    # -----------------------
    import time
    import RPi.GPIO as GPIO
    
    # -----------------------
    # Define some functions
    # -----------------------
    
    def measure():
      # This function measures a distance
      GPIO.output(GPIO_TRIGGER, True)
      time.sleep(0.00001)
      GPIO.output(GPIO_TRIGGER, False)
      start = time.time()
    
      while GPIO.input(GPIO_ECHO)==0:
        start = time.time()
    
      while GPIO.input(GPIO_ECHO)==1:
        stop = time.time()
    
      elapsed = stop-start
      distance = (elapsed * 34300)/2
    
      return distance
    
    def measure_average():
      # This function takes 3 measurements and
      # returns the average.
      distance1=measure()
      time.sleep(0.1)
      distance2=measure()
      time.sleep(0.1)
      distance3=measure()
      distance = distance1 + distance2 + distance3
      distance = distance / 3
      return distance
    
    # -----------------------
    # Main Script
    # -----------------------
    
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)
    
    # Define GPIO to use on Pi
    GPIO_TRIGGER = 23
    GPIO_ECHO    = 24
    
    print "Ultrasonic Measurement"
    
    # Set pins as output and input
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
    GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
    
    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)
    
    # Wrap main content in a try block so we can
    # catch the user pressing CTRL-C and run the
    # GPIO cleanup function. This will also prevent
    # the user seeing lots of unnecessary error
    # messages.
    try:
    
      while True:
    
        distance = measure_average()
        print "Distance : %.1f" % distance
        time.sleep(1)
    
    except KeyboardInterrupt:
      # User pressed CTRL-C
      # Reset GPIO settings
      GPIO.cleanup()

This script can also be downloaded onto your Pi directly using this command line :
    
    
    wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/ultrasonic_2.py

This can then be run using :
    
    
    sudo python ultrasonic_2.py

This will give you a command line that looks something like this :

Obviously your measurements will depend on what you point your sensor at!

Here are some of my other articles you might find interesting if you enjoyed this one :
