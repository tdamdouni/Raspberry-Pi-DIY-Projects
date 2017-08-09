# GPIO Zero Test Drive – Making Light of Security

_Captured: 2017-03-04 at 23:14 from [raspi.tv](http://raspi.tv/2015/gpio-zero-test-drive-making-light-of-security)_

![GPIO Zero based security light](http://raspi.tv/wp-content/uploads/2015/10/GPIO-zero-security-light-150x150.jpg)

Giving GPIO Zero (Beta version) a test drive might make you feel a little insecure, but I'm aiming to throw some light on the situation. I decided to try out some of the built-in features of GPIO Zero by working up a little hardware project. I looked at the current feature set and decided to try and combine MotionSensor, LED and LightSensor all at once. What sort of project uses that kind of technology? Why a PIR-controlled security light of course - if you swap the LED for a relay and 12V lamp! The video will give you an overview of what's going on. If you want to have a go at something similar, or find out how I did it, read on after the video…

### Installation

On a brand new Raspbian Jessie install, I first updated/upgraded…

`sudo apt-get update  
sudo apt-get upgrade`

Then started to install GPIO zero with…

`sudo pip install gpiozero  
sudo pip-3.2 install gpiozero`

The SPI driver 'spidev' install failed to begin with. This was cured by installing python-dev, which is often needed when you are compiling/installing python software that isn't via 'apt-get'…

`sudo apt-get install python-dev python3-dev`

…then I removed GPIO Zero and reinstalled it again…

`sudo pip uninstall gpiozero  
sudo pip install gpiozero`

…and thereafter it worked perfectly.

Don't forget this is a Beta release and future releases will be part of Raspbian. So when it's a finely polished package, this will be a non-issue.

OK. So now we have GPIO Zero installed, we'll need to wire up our circuit and write some code. Let's do the circuit next, then the code.

### Circuit Diagram

Here's what the circuit looks like…

![Circuit for GPIO Zero PIR/LDR 12V Security Light](http://raspi.tv/wp-content/uploads/2015/10/GPIOZero-PIR-lamp_bb-1024x697.png)

> _Circuit for GPIO Zero PIR/LDR 12V Security Light_

### Python Code

And here's the Python code…

12345678910111213141516171819202122
`# This is a gpiozero test. We're going to make a PIR triggered``# security light``# There's a PIR sensor on GPIO21``# a relay on GPIO25 to switch  power to the 12V lamp``# and an LDR on GPIO26``from` `gpiozero ``import` `LED, MotionSensor, LightSensor``from` `time ``import` `sleep``pir ``=` `MotionSensor(``21``, queue_len``=``1``)``light ``=` `LED(``25``)``ldr ``=` `LightSensor(``26``, queue_len``=``1``)``light.off()``while` `True``:``if` `ldr.wait_for_dark():``pir.when_motion ``=` `light.on``pir.when_no_motion ``=` `light.off``print``(``"dark"``)``if` `ldr.wait_for_light():``pir.when_motion ``=` `light.off``pir.when_no_motion ``=` `light.off``print``(``"light"``)``sleep(``0.2``)`

### Code Walk-through

**Lines 1-6** are comments  
**Lines 7-8** we are importing the functions that we need to use from the _gpiozero_ and _time_ modules  
**Lines 9-11** set up the MotionSensor, LED (relay-controlled light in our case) & LightSensor. I've used `queue_len=1` to get a quicker response from the sensors. It prevents 'averaging' of the sensor output, by forcing it to average just one reading. For MotionSensor, the default has now been changed to 1 for future releases, so this can be omitted.  
**Line 12** we switch off the light to begin with because we've wired it up 'backwards' to get round the relay's inverted logic (explained in more detail below).  
**Lines 13-22** contain our main program loop that carries on for ever.  
**Lines 14-17** if it detects a change from light to dark (14), it turns the light off if no motion is detected (15), and on if motion is detected (16), then it prints out "dark" on the screen (17).  
**Lines 18-21** if it detects a change from dark to light (18), it turns the light off if no motion is detected (19), and also off if motion is detected (20) - it's daylight, so we don't need a security light to come on, then it prints out "light" on the screen (21).  
**Line 22** Causes a 0.2 second pause before we start the loop again.

### How Well Does It Work?

This program currently works fine, but when you try to exit it with CTRL+C it refuses to die. (You can kill it from another terminal window using `top`, `k`, type in the Python process number and then `15` then `q` to exit top). If I had to guess, I'd say it could be something to do with lines 14 and 18 both running repeatedly every 0.2 seconds. (I know, I'm a code vandal.)

The only other 'issue' with it is that I've used the LED class for a relay. The relay boards I'm using have inverted logic. So the switch is closed (ON) when GPIO25 is 0/LOW/False. You can get round this in two ways…

  1. Invert your program logic, so tell it `light.off()` when you want the light to be on. This works well, but is rather confusing to read
  2. Wire up the relay connection 'backwards' so that the power to the lamp is connected to the 'NC' (normally closed) terminal. This enables you to code in the most logical way, but the downside is that your lamp will be powered up the moment you connect its power supply, and won't power down until you tell it `light.off()` in line 12

Normally you would wire up a relay the other way round. But in this case, having tried both aproaches, I favour option 2 - code readability. After all, that's what GPIO Zero is all about. The ideal solution will be to create a 'relay' class in GPIO Zero which will be a lot like the LED class, but with inverted logic.

Obviously if this is done, it will need to have warnings about what sort of electricity NOT to use. I'm using a battery powered 12V lamp here. **You should not under any circumstances use bare relays like these to switch mains electricity at high voltage unless you know exactly what you are doing. (Basically DON'T!)**

But I digress into electrical safety. The main point is that we have here a 16-line program (ignoring the comment lines) that provides all the logic and control needed to mimic a security light like the ones you probably have outside your house. It's quite likely that I have horribly abused the system in my attempts to test three aspects at once. But that's what Beta testing is all about. If everybody always did everything the way the author(s) expected, there would be very few bugs found.

### So How Could We Take It Further?

No matter how much you do, it's always possible to go further. One possible idea would be to make use of the mcp3008 class and add an analog to digital converter (ADC). Then we could read the light sensor (LDR) in a more sophisticated way and possibly even add some analog sensors.

You could also add some code to check the time (if the Pi is internet connected) and only activate during certain times. You could even use it as a time-switch to switch on the light if it's dark and a certain time.

### Summing Up

I enjoyed hacking around with GPIO Zero. As an experienced RPi.GPIO user I sometimes found Zero's constraints a little restrictive (trying to do multiple things at once, in Beta), but that's what you trade for being able to do so much with so few lines of code.

That's the big attraction of GPIO Zero though. The fact that you can get going with just a few lines. For most people, this will outweigh the reduced flexibility. But if you _need_ the flexibility, just 'pop the hood' and use RPi.GPIO, which is currently more suitable for advanced GPIO hackery.

As an exercise in fun, I might now go and see how many lines it takes me to reproduce this functionality in RPi.GPIO. I'll see if I get time to do it.

### _Post-publication edit to add…_

Dave Jones, who's been working on GPIO Zero with Ben, has managed to get an alternative version of this script together in 15 lines (and it's more elegant than mine). It works well and you can CTRL+C out of it too…

> -- Dave Jones (@waveform80) [October 15, 2015](https://twitter.com/waveform80/status/654601154538696704)

123456789101112131415
`from` `gpiozero ``import` `LED, MotionSensor, LightSensor``from` `signal ``import` `pause``pir ``=` `MotionSensor(``21``)``ldr ``=` `LightSensor(``26``)``light ``=` `LED(``25``)``def` `daytime():``pir.when_motion ``=` `None``pir.when_no_motion ``=` `None``light.off()``def` `nighttime():``pir.when_motion ``=` `light.on``pir.when_no_motion ``=` `light.off``ldr.when_light ``=` `daytime``ldr.when_dark ``=` `nighttime``pause()`

### _From GPIO Zero to Zero GPIO_

If you want to be a real smartie-pants, you could point out that this can be done without a Pi or GPIO at all. We know this. After all, most PIR security lights have no Pi in. But, with a Pi controlling it you could send an alarm email/SMS/trigger a buzzer if the light comes on. And anyway, it's fun and educational, so who cares? But my friend Daniel challenged me to reproduce this in 'hardware only', so I have. Here it is…

![Security light circuit in hardware only. Zero lines of code.](http://raspi.tv/wp-content/uploads/2015/10/ZeroPi-PIR-lamp-12V_bb3-e1444987671702-1024x616.png)

> _Security light circuit in hardware only. Zero lines of code._

The hardest part was finding a resistor value that worked to trigger the relay whilst balancing the LDR properly. In the end, 4.7k proved to be the optimum (no equations, just 2 or 3 iterations of 'see if this one works'). Note also that the second relay (K2) has been wired 'backwards' to invert the logic of the PIR output for us.
