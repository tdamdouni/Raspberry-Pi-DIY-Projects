# Pan-Tilt Multi Servo Control

_Captured: 2018-05-12 at 09:21 from [www.instructables.com](http://www.instructables.com/id/Pan-Tilt-Multi-Servo-Control/)_

![Picture of Pan-Tilt Multi Servo Control](https://cdn.instructables.com/FHO/ODR6/JD4UKK52/FHOODR6JD4UKK52.LARGE.jpg?auto=webp&width=933)

![](https://media.giphy.com/media/xUNd9UtMEln59wKF0I/giphy.gif?raw=true)

![](http://www.thebox.myzen.co.uk/Tutorial/Media/PWMan.gif?raw=true)

![](https://exploreembedded.com/wiki/images/5/54/0_LPC1768_PWM.gif?raw=true)

![Picture of Installing the Hw](https://cdn.instructables.com/FUE/WELT/JD4UKPJK/FUEWELTJD4UKPJK.LARGE.jpg?auto=webp&width=565)

![Picture of Installing the Hw](https://cdn.instructables.com/FNI/A41P/JDF24UHT/FNIA41PJDF24UHT.LARGE.jpg?auto=webp&width=635&crop=3:2)

![Picture of Servos Calibration](https://cdn.instructables.com/FFX/O5MO/JD4UL101/FFXO5MOJD4UL101.LARGE.jpg?auto=webp&width=837&crop=3:2)

![Picture of Servos Calibration](https://cdn.instructables.com/FAZ/EXCZ/JD4UKXUT/FAZEXCZJD4UKXUT.LARGE.jpg?auto=webp&width=363&crop=3:2)

![Picture of Servos Calibration](https://cdn.instructables.com/FDY/VQQI/JD4UKXQL/FDYVQQIJD4UKXQL.LARGE.jpg?auto=webp&width=363)

The first thing to do it is to confirm the main characteristics of your servos. In my case, I am using a [ Power Pro SG90](http://akizukidenshi.com/download/ds/towerpro/SG90.pdf).

From its datasheet, we can consider:

  * Range: 180o 
  * Power Supply: 4.8V (external 5VDC as a USB power supply works fine) 
  * Working frequency: 50Hz (Period: 20 ms) 
  * Pulse width: from 1ms to 2ms

In theory, the servo will be on its

  * Initial** Position** (0 degrees) when a pulse of **1ms** is applied to its data terminal 
  * **Neutral Position** (90 degrees) when a pulse of 1.5 ms is applied to its data terminal 
  * Final Position (180 degrees) when a pulse of 2 ms is applied to its data terminal

To program a servo position using Python will be very important to know the correspondent "Duty Cycle" for the above positions, let's do some calculation:

  * Initial Position ==> (0 degrees) Pulse width ==> 1ms ==> Duty Cycle = 1ms/20ms ==> 2.0% 
  * Neutral Position (90 degrees) Pulse width of 1.5 ms ==> Duty Cycle = 1.5ms/20ms ==> 7.5% 
  * Final Position (180 degrees) Pulse width of 2 ms ==> Duty Cycle = 2ms/20ms ==> 10%

So the Duty Cycle should vary on a range of 2 to 10 %.

Let's test the servos individually. For that, open your Raspberry terminal and launch your Python 3 shell editor as "sudo" (because of you should be a "super user" to handle with GPIOs) :
    
    
    sudo python3

On Python Shell
    
    
    >>>

Import the RPI.GPIO module and call it GPIO:
    
    
    import RPi.GPIO as GPIO

Define which pin-numbering schemes you want to use (BCM or BOARD). I did this test with BOARD, so the pins that I used were the physical pins (GPIO 17 = Pin 11 and GPIO 27 Pin 13). Was easy for me to identify them and not make mistakes during the test (In the final program I will use BCM). Choose the one of your preference:
    
    
    GPIO.setmode(GPIO.BOARD)

Define the servo pin that you are using:
    
    
    tiltPin = 11

If Instead, you have used BCM scheme, the last 2 commands should be replaced by:
    
    
    GPIO.setmode(GPIO.BCM)
    tiltPin = 17 

Now, we must specify that this pin will be an "output"
    
    
    GPIO.setup(tiltPin, GPIO.OUT)

And, what will be the frequency generated on this pin, that for our servo will be 50Hz:
    
    
    tilt = GPIO.PWM(tiltPin, 50)

Now, let's start generating a PWM signal on the pin with an initial duty cycle (we will keep it "0"):
    
    
    tilt = start(0)

Now, you can enter different duty cycle values, observing the movement of your servo. Let's start with 2% and see what happens (we spect that the servo goes to "zero position"):
    
    
    tilt.ChangeDutyCycle(2)

In my case, the servo went to zero position but when I changed the duty cycle to 3% i observed that the servo stayed in the same position, starting to move with duty cycles greater than 3%. So, 3% is my initial position (o degrees). The same happened with 10%, my servo went above this value, topping its end on 13%. So for this particular servo, the result was:

  * 0 degree ==> duty cycle of 3% 
  * 90 degrees ==> duty cycle of 8% 
  * 180 degrees ==> duty cycle of 13%

After you finish your tests, you must stop the PWM and clean up the GPIOs:
    
    
    tilt= stop()
    GPIO.cleanup()

The above Terminal print screen shows the result for both of my servos (that has similar results). Your range can be different.

![Picture of Creating a Python Script](https://cdn.instructables.com/FXO/EDGX/JD4UL8SL/FXOEDGXJD4UL8SL.LARGE.jpg?auto=webp&width=518)

![Picture of The Pan-Tilt Mechanism](https://cdn.instructables.com/FF8/XOHC/JD4UKY55/FF8XOHCJD4UKY55.LARGE.jpg?auto=webp)

![](https://images-na.ssl-images-amazon.com/images/I/614VTuvOsEL._SL1100_.jpg?raw=true)

![Picture of The Pan-Tilt Mechanism - Mechanical Construction](https://cdn.instructables.com/FOV/EZFB/JD4UKN3Q/FOVEZFBJD4UKN3Q.LARGE.jpg?auto=webp&width=525)

![Picture of Electrical Pan/Tilt Assembly](https://cdn.instructables.com/FOS/OAT2/JD4UKPKI/FOSOAT2JD4UKPKI.LARGE.jpg?auto=webp&width=933)

![Picture of Conclusion](https://cdn.instructables.com/FXP/MBMJ/JC0U8FVB/FXPMBMJJC0U8FVB.LARGE.jpg?auto=webp&width=607)
