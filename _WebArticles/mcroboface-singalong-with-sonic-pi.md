# McRoboFace singalong with Sonic Pi

_Captured: 2017-09-04 at 19:24 from [rbnrpi.wordpress.com](https://rbnrpi.wordpress.com/project-list/mcroboface-singalong-with-sonic-pi/)_

Click the image below for a video of the project in action

![IMG_4773](https://rbnrpi.files.wordpress.com/2016/06/img_4773.jpg?w=1168)

A few weeks ago I purchased a [picon zero](http://4tronix.co.uk/store/index.php?rt=product/product&product_id=552) interface board from 4Tronix. I had seen a review of this board on the [Raspberry PiPod site](http://www.recantha.co.uk/blog/?p=14715) and I was struck by its versatility. Since them I have put it through its paces, helped by another recent acquisition of a ps3 controller, and readers of my blog will have seen projects to control a [MeArm robot](https://rbnrpi.wordpress.com/project-list/ps3-wireless-controlled-mearm-using-pi-and-4tronix-picon-zero-board/), an [Edukit Buggy](https://rbnrpi.wordpress.com/2016/05/31/ps3-controlled-edikit-robot/) and a [multicolour led](https://rbnrpi.wordpress.com/colour-explorer/) using this card. Two or three days ago I was given a prototype McRoboFace as a freebie. The one area of the Picon Zero card I hadn't tested was its ability to drive a neopixel display. I connected the face to the Picon card and ran the test program supplied with the Picon board,
    
    
    #! /usr/bin/env python
    
    # GNU GPL V3
    # Test code for 4tronix Picon Zero
    
    import piconzero as pz, time
    
    pz.init()
    pz.setOutputConfig(5, 3)    # set output 5 to WS2812
    rev = pz.getRevision()
    print rev[0], rev[1]
    try:
        while True:
            pz.setAllPixels(255,255,255)
            time.sleep(1)
            pz.setAllPixels(0,0,0)
            time.sleep(1)
    except KeyboardInterrupt:
        print
    finally:
        pz.cleanup()

which flashed all the leds on and off. I then had the idea of trying to see if it was possible to use the leds as a kind of light show driven by the Picon Zero. I studied the Picon Zero library supplied with the board, and first worked out how the individual leds could be addressed, and how they were numbered. I also noticed that there was a brightness command that could be applied. Since the picon board also had 4 a/d converts built in, I wondered if it would be possible to to use an audio source fed into an a/d converter with suitable circuitry which could then be used to modulate the brightness of the leds in time to the music. Moreover, as a long time fan and user of Sonic Pi, this seemed to be a good source to supply the music.

First I wrote a program to find out how the leds were arranged on the McRoboFace. I found a command pz.setPixel(n,r,g,b) in the library and wrote a simple bit of code to switch them on one by one from 0 up to 16.
    
    
    #! /usr/bin/env python
    
    #testLedNumbers.py
    # Testing McRoboFace led positions.
    # requires picon zero hardware plus software library
    import piconzero as pz, time
    pz.init()
    pz.setOutputConfig(5, 3) # set output 5 to WS2812 (code 3)
    
    try:
    while True:
    for i in xrange(0,17):
    pz.setPixel(i,0,0,255)
    time.sleep(0.5)
    pz.setAllPixels(0,0,0)
    time.sleep(0.5)
    except KeyboardInterrupt:
    print
    finally:
    pz.cleanup() #reset picon zero board

This gave the following result:

![robonumbers](https://rbnrpi.files.wordpress.com/2016/06/robonumbers.jpg?w=1168&h=876)

Now that I could address the pixels individually, the next thing was to figure out how to feed in the audio. I needed to add a DC bias to the AC audio signal, and so I came up with a simple circuit to do this using components from my junk box. The schematic below shows this, together will all the wiring required for the final project.

![McRoboFaceSchematic](https://rbnrpi.files.wordpress.com/2016/06/mcrobofaceschematic1.png?w=1168&h=658)

You can click the image to see a bigger version, and use back arrow to return afterwards.  
Basically each channel of the stereo signal is fed via a capacitor to one end of a resistor where they are summed together and fed to input channel 0 of the Picon board which is configured as an analogue input. The DC bias is derived from a 10k preset resistor and fed to the junction point via a further 10k resistor. By adjusting the potentiometer, the "rest" value of the A/D converter input can be adjusted, and it is then raised and lowered by the alternating current component of the audio signal. The schematic also shows the connection from the Pico Zero board output 5, which can be configured to drive the NeoPixels. As a belt and braces approach, I have included a small series resistor in the signal line connected to the Data In terminal of the McRoboFace, as I have read that this gives better protection to the leds when the power is applied. The final component of the circuitry is a push button switch which is connected between the signal input of channel 1 on the Picon Board, and ground. This input is configured as a digital input with an internal pull-up resistor giving a high signal when the button is not pressed, dropping to low when it is.

The next stage was to test out the system to see if the brightness could be varied. Initially I used an audio signal from my iMac for testing.

I came up with the code below to try this out:
    
    
    #! /usr/bin/env python
    
    #McRoboFlicker.py
    # Sound controlled McRoboFace by Robin Newman June 4th 2016
    # requires picon zero hardware plus software library
    # see circuitry in article at rbnrpi.wordpress.com
    
    import piconzero as pz, time
    
    pz.init()
    pz.setInputConfig(1,0,True) # used for push button digital input (normally high using internal resistor)
    pz.setOutputConfig(5, 3)    # set output 5 to WS2812
    pz.setInputConfig(0,1)      # set to Analogue used to sample audio
    
    try:
        pz.setAllPixels(128,0,128) #set an initial pixel state
        pz.setPixel(15,0,255,0,False) #eye
        pz.setPixel(16,0,255,0) #other eye
        pz.setPixel(14,0,0,255) #nose
        while True:
            v=pz.readInput(0)# read adc value from audio input
            print(v) #print to terminal
            pz.setBrightness(v) #update brightness
            pz.updatePixels() #update all pixels
            time.sleep(0.01) #short sleep to keep repsonse time good, just enough to allow ctrl-C to get a look in
    
    except KeyboardInterrupt:
        print
    finally:
        pz.cleanup() #reset picon zero board

I ran the program and then started playing some fairly percussive music, which I fed into the circuit, and by carefully adjusting the potentiometer I was able to get the leds flickering in time to the music, although the adjustment was fairly critical, and it only worked well for quite low light levels. This was becuase the fluctuation was fairly small, and thus only had an appreciable effect if the starting light level was low. At this stage I put a short video clip on twitter, and received a reply back from 4Tronix saying "Excellent. Just need to open and close the lips in sync :)" This set me thinking, is that possible? First of all I wrote a little function which would alternate between mouth open and mouth closed. This could be achieved by switching from a state where leds 0-9 where on and leds 10-13 were off, to one where leds 0,5 and 10-13 were on and leds 2-4 and 6-9 where off. The program below illustrated this:
    
    
    #! /usr/bin/env python
    
    # McRoboFaceMouth.py
    # Test code for 4tronix Picon Zero
    
    import piconzero as pz, time
    
    pz.init()
    pz.setOutputConfig(5, 3)    # set output 5 to WS2812
    
    def change(t): #parameter = 1 to open mouth anything else to close it
        #False parameter so all updates done together once set up, when brightness changes
        pz.setPixel(0,128,0,128,False) #end of mouth always this colour
        pz.setPixel(5,128,0,128,False) #other end of mouth
    
        if t==1: #going for open mouth
            for i in xrange(1,5):#mouth set pixels for open state
                pz.setPixel(i,128,0,128,False)
                pz.setPixel(i+5,128,0,128,False)
            for i in xrange(10,14): #pixels for closed mouth turned off
                pz.setPixel(i,0,0,0,False)
        else: #going for closed mouth
            for i in xrange(1,5): #mouth
                pz.setPixel(i,0,0,0,False)
                pz.setPixel(i+5,0,0,0,False)
            for i in xrange(10,14): #pixels for closed mouth turned on
                pz.setPixel(i,128,0,128,False)
        return
    
    try:
        pz.setAllPixels(128,0,128)
        while True:
            change(1)
            pz.updatePixels()
            time.sleep(0.5)
            change(0)
            pz.updatePixels()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print
    finally:
        pz.cleanup()
    
    

The last stage, which took quite a lot of experimentation to get right, was to incorporate the mouth open/close routine into the program which modulated the leds' brightness according to the audio signal. I wanted to achieve some form of synchronisation between the open command and the music, so that they looked as if they were related. However, it was also important to make sure that the mouth remained open for a reasonable length of time, otherwise it was difficult to register visually. Also, I wanted to allow a short gap between the mouth closing and (possibly) being retriggered to open, again for the same reason. I also wanted if possible to get a slightly larger signal to modulate the brightness. I incorporated a button on the breadboard, wired to input 1, which was set up as a digital input, held normally high by an internal resistor on the Picon board. Pressing the button shorted the input to ground, and this signal was detected and used within the final program, to read the "rest" level setting of the A/D converter. This offset was then subtracted from the actual signal level being read as the music played, and the absolute of the resultant was processed with the formula **b=min(100,5*(abs(v-offset))+5) **to give a brightness number **b** ranging from 5 to 100. The 5 ensured that the less never actually went out. When this signal exceeded a threshold level (65) then the routing was triggered to open the mouth. To give further realisation, I used the magnitude of the triggering brightness level to control the number of loop cycles the mouth remained open **openslot=int(b/10)** before closing. Once closed a minimum time **shutslot=2 **to set the number cycles that needed to elapse before the mouth could be triggered to open again. The complete program is shown below:
    
    
    #! /usr/bin/env python
    
    #McRoboFaceSinging.py
    # Sound controlled McRoboFace by Robin Newman June 4th 2016
    # requires picon zero hardware plus software library
    # see circuitry in article at rbnrpi.wordpress.com
    #version 1.2
    import piconzero as pz, time
    
    #setup piconzero card
    pz.init()
    pz.setInputConfig(1,0,True) # used for push button digital input (normally high using internal resistor)
    pz.setOutputConfig(5, 3)    # set output 5 to WS2812
    pz.setInputConfig(0,1)      # set to Analogue used to sample audio
    
    #initialise variables used by the program
    v=0 #adc value
    offset=0 #rest adc value read when button pushed
    opencount=0 #count cycles between shutting and next opening of mouth
    shutcount=0 #count cycles between opening and next shutting of mouth
    openFlag=0 #0 closed, 1 open
    b=0 #current brightness
    threshold=65 #trigger brightness level to open mouth
    blast=0 #last brightness
    openslot=8 #number of cycles for which mouth remains open (initial value)
    shutslot=2 #number of cycles for which mouth remains closed (I have had this higher at 4: experiment with it!)
    
    #define function to open or close mouth
    def change(t): #parameter = 1 to open mouth anything else to close it
        #False parameter so all updates done together once set up, when brightness changes
        pz.setPixel(0,128,0,128,False) #end of mouth always this colour
        pz.setPixel(5,128,0,128,False) #other end of mouth
    
        if t==1: #going for open mouth
            for i in xrange(1,5):#mouth set pixels for open state
                pz.setPixel(i,128,0,128,False)
                pz.setPixel(i+5,128,0,128,False)
            for i in xrange(10,14): #pixels for closed mouth turned off
                pz.setPixel(i,0,0,0,False)
        else: #going for closed mouth
            for i in xrange(1,5): #mouth
                pz.setPixel(i,0,0,0,False)
                pz.setPixel(i+5,0,0,0,False)
            for i in xrange(10,14): #pixels for closed mouth turned on
                pz.setPixel(i,128,0,128,False)
        return
    
    try:
        pz.setAllPixels(128,0,128) #set an initial pixel state
        pz.setPixel(15,0,255,0,False) #eye
        pz.setPixel(16,0,255,0) #other eye
        pz.setPixel(14,0,0,255) #nose
        while True:
            #adjust counters depending upon whether mouth open or closed
            if openFlag==1:
                opencount +=1 #increase count of number of cycles mouth is open
            else:
                shutcount+=1 #increase count of number of cycles mouth is closed
    
            if (b>threshold) and (shutcount>shutslot) and (openFlag==0): #open mouth triggered by audio
                opencount=0 #reset count to 0 
                openslot=int(b/10) #set openslot cycles according to brightness
                openFlag=1 #opening so set flag
                change(1) #open mouth
    
            else:
                if (opencount >openslot) and (openFlag==1 and b<threshold-20): #ensures stays open for at least openslot cycles
                      openFlag=0 #closing so reset flag
                      #shutslot=2 #doesn't change. set in intialisation
                      shutcount=0 #reset shutcount
                      change(-1) #close mouth
             #now process brigthness level
             v=pz.readInput(0)# read adc value from audio input
             b=min(100,5*(abs(v-offset))+5) #calcuate next brigthness
             print(b) #print to terminal
             #check for pffset calibration button
             trigger=pz.readInput(1) #check for button pressed
             if trigger==0: #normally high: 0 if pushed
                offset=v #update offset value from current adc value
             #now adjust brightness if changed sufficiently
             if abs(blast-b)>10: #check if brightness has changed by at least 10 to reduce noise
                pz.setBrightness(b) #update brightness
                pz.updatePixels() #update all pixels
                blast=b #save brightness value
    
            time.sleep(0.01) #short sleep to keep response time good, just enough to allow ctrl-C to get a look in
    
    except KeyboardInterrupt:
        print
    finally:
        pz.cleanup() #reset picon zero board
    
    

There are numerous comments in the program which should enable you to work out the logic of what is happening. In use, the program should be run without an audio signal present. Then adjust the 10K potentiometer from minimum to set a point just above the limit of 100 shown on the screen. Press the calibration button, which will then subtract the offset, causing the leds on the McRoboFace to dim, and the brightness level shown on the screen to drop to a low fluctuating value, which should be insufficient to trigger the mouth changing. Now start the audio feed, and the face should spring into singing action, with the leds flickering in brightness according to the music amplitude and the mouth being triggered to open and close.

**Construction**

Below is an image of the layout I used on a breadboard for the components. You can click to enlarge it, and return using the back button on your browser:

![McRoboFaceSinging](https://rbnrpi.files.wordpress.com/2016/06/mcrobofacesinging.png?w=1168&h=658)

I used components I had to hand, but the capacitor values are not too critical and you can try higher or lower, similarly the 10K fixed resistor could probably by a bit lower if that is what you have to hand. Rememer that electrolytic capacitors are polarity conscious. Connect the +ve side to the resistor, and the -ve to the audio inputs.

In developing the circuit, I occasionally found that the piconzero locked up, probably before I had got all the input values fed to the A/D converter under control. If that happens to you, you need to shut down AND REMOVE POWER from the computer and board and then restart. The symptom is that the program runs, but no output appears on the terminal screen.

Below are a series of photos which may aid the construction of the breadboard layout:

![IMG_4763](https://rbnrpi.files.wordpress.com/2016/06/img_4763.jpg?w=1168&h=876)

![IMG_4764](https://rbnrpi.files.wordpress.com/2016/06/img_4764.jpg?w=1168&h=876)

![IMG_4765](https://rbnrpi.files.wordpress.com/2016/06/img_4765.jpg?w=1168&h=876)

![IMG_4766](https://rbnrpi.files.wordpress.com/2016/06/img_4766.jpg?w=1168&h=876)

![IMG_4768](https://rbnrpi.files.wordpress.com/2016/06/img_4768.jpg?w=1168&h=876)

![IMG_4769](https://rbnrpi.files.wordpress.com/2016/06/img_4769.jpg?w=1168&h=876)

![IMG_4771](https://rbnrpi.files.wordpress.com/2016/06/img_4771.jpg?w=1168&h=876)

![IMG_4772](https://rbnrpi.files.wordpress.com/2016/06/img_4772.jpg?w=1168&h=876)

![IMG_4773](https://rbnrpi.files.wordpress.com/2016/06/img_4773.jpg?w=1168&h=876)

The Picon Zero board is available from <http://4tronix.co.uk> and they hope to lunch McRoboFace as a kickstarter project very soon. They also sell breadboards and sets of leads.

The programs in this article can be downloaded from [here](https://gist.github.com/rbnpi/2c3618ed214d5bd79f2e6199f5a5318e)

A video of the project in action is [here](https://youtu.be/bp6JeHgJFdY)
