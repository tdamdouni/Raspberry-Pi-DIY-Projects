# Raspberry Pi Beginners Tutorial 7: Using a Passive Buzzer

_Captured: 2017-09-29 at 20:13 from [componentsplus.co.uk](http://componentsplus.co.uk/tutorials/raspberry-pi-tutorials-and-guides/getting-started/tutorial-7-using-a-passive-buzzer)_

**The Raspberry Pi can generate a frequency which can be used to power a small buzzer.**

Using the buzzer, build the following circuit:

![Using a Passive Buzzer with a Raspberry Pi Schematic Wiring Diagram](http://componentsplus.co.uk/images/tutorial-7-using-a-passive-buzzer-with-a-raspberry-pi-schematic-wiring-diagram.jpg)

Open** IDLE** on your Raspberry Pi (Menu > Programming > Python 2 (IDLE)) and open a new project (File > New File). Then type the following:

> 
>     gpin=18
>     import RPi.GPIO as GPIO
>     import time
>     from sys import argv
>     freq=argv[1]
>     GPIO.setmode(GPIO.BCM)
>     GPIO.setup(gpin, GPIO.OUT)
>     GPIO.output(gpin, False)
>     
>     
>     timeunit=1/float(freq)
>     print(timeunit)
>     while True:
>             GPIO.output(gpin, True)
>             time.sleep(timeunit)
>             GPIO.output(gpin, False)
>             time.sleep(timeunit)
>     

Save your project as** buzzer.py** (File > Save As) in your Documents folder.

Now open **Terminal** (Menu > Accessories > Terminal) and type the following command:

> 
>     python buzzer.py 10000

The buzzer will emit a high pitch tone of 10 khz (10,000 hertz). This is because the Raspberry Pi is sending around 10,000 electrical pulses to the buzzer every second. Since the Raspberry Pi's processor is already focussing on many other tasks (including running Raspbian) it is unable to send these pulses consistently. As a result, the pitch isn't exactly perfect.

You can stop this program from running by pressing **CTRL+Z**.

Now type the following command to create a lower tone of 800 hertz will be emitted:

> 
>     python buzzer.py 800

This script uses Python's command line arguments feature to import the value you specified when typing the command. The command **freq=argv[1]** stores the provided value in the freq parameter.
