# Add an off-switch to power down your Pi

_Captured: 2017-11-10 at 00:50 from [www.raspberrypi.org](https://www.raspberrypi.org/magpi/off-switch-raspberry-pi/)_

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/05/raspi2.jpg)

To keep prices down, the Raspberry Pi is missing something that most electronic devices come with: a switch to turn it on and off. That's OK, you say, we'll just pull the plug to turn it off. Unfortunately, this can lead to corruption problems with the SD card. All the instructions say you should run the shutdown command before pulling the plug, but this is not always possible, particularly when your Raspberry Pi is running headless without a connected keyboard and monitor, and possibly even without a network connection. So, what can a self-respecting DIYer do? The answer, of course, is 'add your own switch'!

_The full article can be found in [The MagPi 57](https://www.raspberrypi.org/magpi/issues/magpi/57) and was written by Tony Hansen._

Lots of articles are available to tell you how to use a breadboard to connect a button or LED to a Raspberry Pi's GPIO pins. This article focuses on doing something useful with those switches and LEDs.  
The safe off-switch is complementary to a reset switch, which is the best method for starting the Raspberry Pi up again. Issue 52 of The MagPi featured an excellent article on how to connect a reset button.

### You'll need

Momentary push button switches

### Using GPIO Zero

With the GPIO Zero library, the Python code to deal with a button press becomes extremely simple. Assuming your button is connected between GPIO 21 and GND (ground), the code is nice and easy. You can download it from [the Git repo](https://github.com/TonyLHansen/raspberry-pi-safe-off-switch/) as shutdown-press-simple.py.

This code creates a button on GPIO 21, waits for it to be pressed, then executes the system command to power down the Raspberry Pi. GPIO 21 is nice because it's on pin 40 of the 40-pin header and sits right next to a ground connection on pin 39. This combination makes it difficult for an off-switch to be plugged in incorrectly. On a 26-pin header, GPIO 7 is similarly situated at the bottom, on pin 26, next to pin 25's ground connection.

Create the script on your Raspberry Pi using your favorite text editor (e.g., nano, Vim or Emacs), as in:

Then add a line to the end of /etc/rc.local to run it at boot time:

Now, after rebooting, your script will be running and listening for a button (connected between GPIO 21 on pin 40 and ground) to be pushed.

### Preventing accidental button pushes

One major drawback of the previous code is that any accidental push of the button will shut your Raspberry Pi down. It would be better if you needed to hold the button down for several seconds before everything powers down. Check out shutdown-with-hold.py.

Instead of hard-coding the GPIO number 21 and the hold time, this code does a few things differently. First, it defines variables to hold these numbers at the top of the code. For a program this small, declaring the values at the top is not necessary, but it is good practice to declare any configurable variables near the top of the code. When making changes later, you won't have to hunt through the code to find these variables. Secondly, it allows the GPIO number and hold time to be overridden on the command line, so that you can change them later without modifying the program.

We then define a function named shutdown() to execute the poweroff system command. The button is also assigned to a variable for use in the next statement. This time, we are also specifying that the button must be held down, and when the hold time (6 seconds) has passed, any function assigned to the when_held event will be executed. We then assign that event to the shutdown() function we defined earlier. The call to pause() is needed to cause the script to wait for the button presses.

If you look at the examples that come with the GPIO Zero source, you'll find a script very similar called [button_shutdown.py](https://github.com/RPi-Distro/python-gpiozero/blob/master/docs/examples/button_shutdown.py).

### Feedback while pressing the button

We can do better. The major thing lacking with the above code is any sort of feedback. It is hard to tell that anything is really happening while you have the button pressed down. Fortunately, GPIO Zero allows us to do much more with a button press, such as turning an LED on and off or setting it blinking, by attaching this to the button's when_pressed event.

We need to ensure that the LED is turned off if the button is not held down for the entire length of time. This can be accomplished by attaching to the when_released event.

As before, the important work has been moved into functions named when_pressed(), when_released(), and the same shutdown() function we used before. These are assigned to their corresponding button events.

### Going further

Can you think of other ways to provide feedback while pressing the hold button, or alternative ways to signal that it is time to turn off? How about using a buzzer, or popping up a message on a screen? You could also use the on-board activity LEDs, making them blink faster and faster as it gets closer to shutdown time. Or even play an audio clip, such as "I'm melting". The GitHub repository contains additional examples such as these. How about watching the 'low battery' signal from a battery pack as a signal to shut down? Let your imagination run wild.

Now, which of your projects are you going to add shutdown and reset buttons to?
