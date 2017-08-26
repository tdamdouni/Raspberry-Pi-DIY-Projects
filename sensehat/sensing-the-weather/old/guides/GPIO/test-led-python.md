# Test your LED with Python

1. With your circuit complete, you are now ready to write some code to switch the LEDs on. Boot your Raspberry Pi, login and type `startx`.

1. Click on the **Terminal** application icon on the taskbar or click on the **Menu** followed by **Accessories** and then select **Terminal** with your mouse pointer. The icon for **Terminal** looks like this:

    ![](images/terminal-icon.png)

    Once loaded type `sudo idle3 &` and press enter on the keyboard. This will load the Python 3 programming environment called `IDLE3` as the super user which allows you to create a program that affects the GPIO pins. Once loaded click on **file** and **new window**.

1. Save the file by clicking on **file** and **save as**. Name your file `led-on-off.py`.

1. Next type the following code:

    ```python
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    ```
    *The first two lines tells the Python interpreter (the thing that runs the Python code) that it will be using a ‘library’. You will need the `time` library in order to add timings to your program and the `RPi.GPIO` library that will tell the Pi how to work with the Raspberry Pi’s GPIO pins. A ‘library’ gives a programming language extra commands that can be used to do something different that it previously did not know how to do. This is like adding a new channel to your TV so you can watch something different. Each pin on the Pi has several different names, so you need to tell the program which naming convention is to be used in the second line of the code. The final line tells Python not to print GPIO warning messages to the screen.*
    
1. Underneath type:

    ```python
    print("Light on")
    GPIO.output(18,GPIO.HIGH)
    ```
    *The `print` function prints some information to the terminal. This is handy as it tells you what is happening, so that even if you LED doesn't come on you know that your program is working. If that happens then there might be something wrong with the wiring of your circuit and you should go back through the steps above to check.*
    
    *The next line turns the GPIO pin 18 ‘on’. What this actually means is that this pins is made to provide power of 3.3volts. This is enough to turn the LED in your circuit on.*
    
1. The code so far will turn on the LED, let's add some code to turn it off after a period of time. Below type:

    ```python
    time.sleep(3)
    print("Light off")
    GPIO.output(18,GPIO.LOW)
    ```
    *The first line adds a pause or sleep. It tells the program to sleep for 3 seconds before moving onto the next line in the sequence of code. During this time your LED will be on because you have not told it to do anything else yet. To turn the LED off, you add a line similar to the one that turned GPIO pin 18 on by making it high, instead you replace GPIO.HIGH with GPIO.LOW. This will turn the pins off so that they no longer supply any voltage.*

1. The final part to add to your program is:

    ```python
    GPIO.cleanup()
    ```
    
    *The GPIO.cleanup() command at the end is necessary to reset the status of any GPIO pins when you exit the program. If you don’t use this, then the GPIO pins will remain at whatever state they were last set to.*

1.	Save your code by clicking on **file** and **save**.

1. It is now the moment of truth! Click on **run** and **run module** to execute (or run) your code. 

