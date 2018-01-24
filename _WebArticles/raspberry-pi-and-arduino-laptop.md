# Raspberry Pi and Arduino Laptop

_Captured: 2017-11-09 at 13:10 from [www.hackster.io](https://www.hackster.io/BuildItDR/raspberry-pi-and-arduino-laptop-bf50f5)_

![Raspberry Pi and Arduino Laptop](https://hackster.imgix.net/uploads/attachments/375791/f8k0lugj9ow8e1l_medium_M3x0Gb1bky.jpg%3Fauto%3Dcompress%252Cformat?auto=compress%2Cformat&w=900&h=675&fit=min)

Since the day I heard about and got to play with the Raspberry Pi one a few years ago I've wanted to make a Raspberry Pi powered laptop out of it and now with the rease of the Raspberry Pi three I've decided to finally see it through. Now this isn't my first time attempting to make a fully working laptop using a Raspberry Pi, every other time I've tried the project has been riddled with errors with anything from broken ribbon cables to figuring out the hinge mechanism however I've been able to learn from these failures and I hope to show you how to avoid them when making your own. So lets get started!

![](https://hackster.imgix.net/uploads/attachments/375780/F60IVZWJ9OW8BMB.MEDIUM.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Before we can start choosing and buying the parts we are going to be using we need to figure out everything we want our laptop to be able to do, for example I want my laptop to have:

  * integrated mouse (trackpad) 
  * long battery life 
  * at least 2 USB ports 
  * full keyboard 
  * integrated Arduino powered battery reader 
  * integrated Arduino with headers for plugging components into 
  * small form factor

Since we are using the Pi 3 we dont have to worry about buying a Wifi or Bluetooth dongle because it has it all integrated. Now this list is by no means exclusive, there are many other things that can be added to make this a better laptop however I think the features im adding will give it some awesome usability such as the integrated Arduino powered battery reader which will be a small OLED screen next to the main screen which will permanently show the battery percent and voltage, another feature I really like is the integrated Arduino with headers, this is basically an Arduino with male headers soldered to it, there are small holes cut in the case that allow the user to access the male pins and plug in components, so all this really is just an Arduino built into the laptop so we always have an Arduino handy.

![](https://hackster.imgix.net/uploads/attachments/375781/FMPBNBEJ9OW89SL.MEDIUM.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

For this project we will need quite a lot of parts, we will need:

  * Reinforced cardboard

We are also going to need the trackpad we made in a previous project, you can find the full tutorial [ here](https://www.youtube.com/watch?v=ssTFgNUH_qk) . Once again this is by no means an exclusive list, whats nice about these parts is that the majority arent dependent on each other so you can swap parts for whatever you want. We have **alot **of parts to setup so to make it easier we are going to set them up individually and then at the end we can put them all together.

![](https://hackster.imgix.net/uploads/attachments/375782/FDYKRMQJ9OW8BO9.MEDIUM.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Lets start with our PI and screen, our screen doesn't connect to our Pi through the HDMI port but rather through a 50 pin ribbon cable that plugs into the Pis GPIO however if you just plug it in and start up the Pi it won't work, we need to edit some lines of code in the startup file for the Pi.

We start this by downloading a fresh Raspbian image [ Here ](https://www.raspberrypi.org/downloads/raspbian/), then we write it to our SD card using 7Zip (or whatever software works for you). Now once its written we need to open a file on the SD card called **config.txt** and add some code. What this code does is tell the Pi to send the screen data through the GPIO headers rather than the HDMI port (HDMI is the default) on startup. Putting the code in is really easy. Open the config.txt with a notepad program, for windows i'm using notepad ++, and copy this code into the config.txt file now save and close and it should work once the SD card is plugged back into the Pi. If it looks too bright or too dim turn the little petentiomoter on the screen circuit board until it looks right.

Our Pi also needs to physical modification to fit inside our case properly we are going to have to desolder one of the duel usb ports, this is done by putting a fairly large amount of solder on the pins of the USB connector and slowly rocking it back and forth until it becomes free. We do this because we need to solder a usb hub to the Pi to plug in all of our input devices.

The code:
    
    
    <p>dtoverlay=dpi24<br>enable_dpi_lcd=1
    display_default_lcd=1
    dpi_group=2
    dpi_mode=87
    dpi_output_format=0x6f005
    hdmi_cvt 1024 600 60 6 0 0 0</p>
    

![](https://hackster.imgix.net/uploads/attachments/375783/FUI3UIVJ9OW89VN.MEDIUM.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Our battery uses 3 18650 batteries that have a capacity of 2400 mAh each, in parallel the 3 cells have a total capacity of 7200 mAh, our pi with everything plugged in draws around 1 Amp meaning our 3 cells can power the pi for roughly 4.5 - 5 hours but this can be increased by adding more batteries if you want. To build it we need to charge all 3 cells all the way up to 4.2 volts individually as connecting lithium cells is very dangerous if they have different charge states (different voltages) to avoid this its easiest to make sure they are all fully charged before connecting them.

Now we want to connect these cells in parallel to do this we connect all the positive terminals together and then connect all the negative terminals together, use thick wire as a lot of current might pass between these batteries which would heat up a thinner wire. now connect the negative and postie terminal of the batteries to the negative and positive input terminals of the power bank circuit respectively and thats all for the battery!

Instead of using a power bank circuit like I've used here you could use a lithium charger to charge the cells to 4.2 volts and boost converter to boost the 4.2 volts to 5 volts but this will ultimately do the exact same thing as the power bank circuit and would take up more space.

![](https://hackster.imgix.net/uploads/attachments/375784/FHX61B7J9OW8A2N.MEDIUM.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Now to set up the battery display, this step is defiantly not that necessary as you could read the battery voltage through the Pis GPIO and display the battery level through software, however, I wanted to add this because I think the OLED screen gives the whole laptop a really cool DIY look. To make it we need to solder our OLED screen to our Arduino, the OLED im using is not an SPI version so I have to solder 7 pins to the Arduino.

The pinout is as follows:

  * OLED-------------------Arduino
  * Rest - Pin 7
  * DC - Pin 12
  * CS - Pin 9
  * DIN - Pin 11
  * CLK - Pin 13
  * VCC - 5 Volts
  * Ground - Ground

Before we can upload our code we have to make our voltage probes which will connect the Arduino to the battery and allow it to read the batteries voltage we need to solder 2 10 ohm resistors in a voltage divider configuration (see photos) to the A0 and Ground pins on the Arduino which can then be connected to the battery, A0 goes to positive and Ground goes to Ground. We also need a power source for our screen so we need to solder another wire to ground and one to VIN on the Arduino which we will connect to the power bank circuit later for power.

Finally, we can upload our code which can be found below.

![](https://hackster.imgix.net/uploads/attachments/375785/FJ0CVS9J9OW89VO.MEDIUM.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

So we've set up all the main parts and now all we need to set the smaller and easier parts. Starting with the keyboard, we need to remove it from the casing it came in (its intended to be used with a 7inch tablet) all we need to do is cut the fake leather around the keyboard and pull it and its circuit out, its that easy youll see there are 4 wires which we will solder to our USB hub later.

The track-pad also need minimal setup as all we need to do is take this one we made in a previous project and get a micro USB cable to plug it into our USB hub, you can see how this was made [here](https://www.youtube.com/watch?v=ssTFgNUH_qk) .

Lastly our internal Arduino will need to have headers soldered onto all of its pins, its easiest to do this by putting these pins and the Arduino onto a breadboard and then soldering them in place as this will keep them straight, then we just get another micro USB cable to connect the Arduino to the USB hub. Now everything is set up so we can start putting things together!

At this point we have individually put all the parts together now we need to connect them to each other to make the internals of our laptop.

We start by connecting the USB hub to one of the two USBs that we desoldered earlier, the second USB is then soldered to a female USB port which is placed on the other side of the laptop using some long wires, now solder the track-pad, Keyboard and internal Arduino to the USB hub. Next we solder the 5 volt output of our power bank circuit to the 5 volt input on the raspberry pi using a micro USB cable or even the dedicated 5 volt and ground solder pad that can be found under the Pi.

This is everything for the base now we can move onto the screen half there are only 2 parts in our screen, the main screen and battery display, all we need to do is connect the 50 pin ribbon cable to the main screen and to the 50 pin connector on the raspberry pi. Next we need to run 3 long cables from from the Arduino battery display, these are the battery read and power cables which we spoke about earlier, the cable connected to pin A0 get connected to the positive connection on the battery, the VIN pin gets connected to 5 volt output on the power bank circuit and ground goes to ground.

Of course at some point we might want to turn this off so we are going to add a switch in between the ground connection from the power bank to the raspberry pi which allows us to completely cut power to the system. I do need to note that just cutting power to the raspberry pi is bad for it so preforming a software power down before cutting power is ideal, this can be done by just clicking shut down in the raspberry pi options.

![](https://hackster.imgix.net/uploads/attachments/375786/F19IT26J9OW8ANI.MEDIUM.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Now unfortunately i don't have a 3D printer but we can make a very sturdy and nice looking (my opinion) case from some malleable plastic and cardboard. The idea behind this is that the walls of the case will be made of a cardboard with the malleable plastic being used inside the case to keep everything together and make it sturdier. the key to doing this is measuring out the sizes of cardboard needed and cutting it out, the cardboard is then glued together with super glue, using hot glue at this point often leaves a visible lines which looks very ugly, the best think to do is put the pieces together using super glue and the reinforce it with hot glue on the inside followed by a layer of the malleable plastic. Ive left the dimensions for my case here if you choose to go this route however if you have a 3D printer i do think that is the neater options (let me see how it turns out in the comments!).

![](https://hackster.imgix.net/uploads/attachments/375787/FKI1VETJ9OW8BI3.MEDIUM.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Weirdly enough I found this part of the project to be the hardest even though it seems like such an easy part. What we need to do is get a very stiff hinge, I know its easier said than done but a good place to start looking is in old laptops or screen, you can find these for next to nothing at ewaiste facilities. once you have your hinge make a notch of the bottom of the screen and in the top of the base and full these notches with the malleable plastic I spoke about earlier. Now while its still warm and malleable begin pushing the hinge into it and secure it in place, because this stuff dries so hard there will be no issues with the hinge ever coming loose. If you make a mistake a hairdryer can be used to re melt the protoplatic and it can then be reshaped or removed.

![](https://hackster.imgix.net/uploads/attachments/375788/FLX0KLGJ9OW89WY.MEDIUM.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

While making this project I ran into quite a few issues that slowed me down or could have costed me a lot of money, the first and most annoying was the ribbon cable. Ribbon cables aren't designed to be plugged in and unplugged many times and unfortunately this is something I do a lot of while testing which actually broke mine from wear and tear (i ordered a new one) so make sure to be very careful with it. Another thing that annoyed me while testing this laptop was that I kept uploading code to the wrong internal Arduino! in the base we have 2 Arduinos plugged into the raspberry pi the first is the one controlling the trackpad and the second one is the Arduino we installed to used as an internal Arduino, the annoyance arises when I accidentally upload my sketch to the track-pad Arduino rather than the Arduino I wanted to upload it to, this of course messes with our track-pad making it unusable until we upload its code again so just make sure you know which Arduino is which in the Arduino IDE.

With all of that being said i have to say this isnt a very challenging project as there was minimal code required and the people over at the Raspberry Pi foundation have made the process of getting the Pi set up and working really easy.

At this point the laptop is fully functional, i've been using mine almost everyday for taking notes, it works great for this as the Raspbian OS comes with libraoffice so using this as a school or work laptops is a really good idea. It also connects to WiFi and Bluetooth networks really easily making watching YouTube and other webpages really easy and to make it even better there are lots and lots of games that will run on the raspberry pi with anything from minecraft to classic old NES games making great fun with a long battery life. Overall this is a really fun project and I really recommend trying it.

If you have any questions please comment or send me a message and ill try my best to get back to you.

```
<p>dtoverlay=dpi24<br>enable_dpi_lcd=1
display_default_lcd=1
dpi_group=2
dpi_mode=87
dpi_output_format=0x6f005
hdmi_cvt 1024 600 60 6 0 0 0</p>
```
