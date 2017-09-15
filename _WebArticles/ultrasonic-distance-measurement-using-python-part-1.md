# Ultrasonic Distance Measurement Using Python – Part 1

_Captured: 2017-09-09 at 16:45 from [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/)_

![Ultrasonic Sensor Circuit](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/12/Ultrasonic-Sensor-01-702x336.jpg)

LEDs, buzzers and switches are the most common items people attempt to interface to their Raspberry Pi's. Something I found in eBay that is a little bit different is an ultrasonic measurement module. This allows you to measure the distance to the nearest wall or solid object. The modules are easy to buy, cheap and relatively straight forward to interface to the GPIO header.

So here is some information on my experiments with an Ultrasonic measurement module and Python. In future projects I can see these modules being a great way to add some intelligence to a Pi powered robot or car.

The HC-SR04 module cost approximately £3 ($5) and is the size of a box of matches. The two transducers give it a distinctive appearance. It is designed to be powered by 5V, has 1 input pin and 1 output pin. The module works by sending an ultrasonic pulse into the air and measuring the time it takes to bounce back. This value can then be used to calculate the distance the pulse travelled.

## Connecting To The Pi

Powering the module is easy. Just connect the +5V and Ground pins to Pin 2 and Pin 6 on the Pi's GPIO header.

The input pin on the module is called the "trigger" as it is used to trigger the sending of the ultrasonic pulse. Ideally it wants a 5V signal but it works just fine with a 3.3V signal from the GPIO. So I connected the trigger directly to Pin 16 (GPIO23) on my GPIO header.

You can use any GPIO pins you like on your RPi but you will need to note the references and amend your Python script accordingly.

The module's output is called the "echo" and needs a bit more thought. The output pin is low (0V) until the module has taken its distance measurement. It then sets this pin high (+5V) for the same amount of time that it took the pulse to return. So our script needs to measure the time this pin stays high. The module uses a +5V level for a "high" but this is too high for the inputs on the GPIO header which only like 3.3V. In order to ensure the Pi only gets hit with 3.3V we can use a basic voltage divider. This is formed with two resistors.

If R1 and R2 are the same then the voltage is split in half. This would give us 2.5V. If R2 is twice the value of R1 then we get 3.33V which is fine. So ideally you want R2 to be between R1 and R1 x 2. In my example circuit I used 330 and 470 ohm resistors. An alternative would be to use 1K and 1K5 values.

Here is a diagram of my final circuit. I chose GPIO23 and GPIO24 but you can use any of the 17 available GPIO pins on the GPIO header. Just remember to update the script.

Here is a photo of my circuit. I used a small piece of breadboard and some male-to-female jumper cables.

## Python Script

Now for the script to actually take some measurements. In this example I am using Python. Why Python? It's my favourite language on the Pi so I tend to use it for all my experiments but the technique here can easily be applied to C.

You can either download the script directly using [this link](https://www.raspberrypi-spy.co.uk/archive/python/ultrasonic_1.py) or via the command line on the Pi using :
    
    
    wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/ultrasonic_1.py

This can then be run using :
    
    
    sudo python ultrasonic_1.py

## Speed of Sound

The calculation that is used to find the distance relies on the speed of sound. This varies with temperature. The scripts calculate the correct value to use based on a pre-defined temperature. You can change this value if required or perhaps measure it dynamically using a temperature sensor.

## Photos

Here are some photos of my ultrasonic sensor connected to Raspberry Pi via the GPIO header :

## Accuracy

Here are some points about accuracy :

  * The accuracy of the distance measurement is dependent on timing. Python under Linux is not ideal for precise timing but for general messing about it will work OK. To improve accuracy you would need to start looking at using C instead.
  * When the GPIOs are configured the module needs some time before it is ready to take its first reading so I added a 0.5 second delay to the start of the script.
  * The transducers have a wide angle of sensitivity. In a cluttered environment you may get shorter readings due to objects to the side of the module.
  * Measurements work down to about 2cm. Below this limit the results can give strange results.
  * If the ultrasonic transducers touch anything the results are unpredictable.

Thanks to this technology I now know that the distance from my desk to the ceiling is 155cm.

### Update

If anyone wants to experiment with these devices in C then check out this page :  
<http://rasathus.blogspot.co.uk/2012/09/ultra-cheap-ultrasonics-with-hy-srf05_27.html>  
It also includes a comparison between Python and C implementations.

### Credits

Thanks to Leroy Milamber for correcting an error in my code.

Here are some of my other articles you might find interesting if you enjoyed this one :
