# Flotilla-controlled Raspberry Pi internet radio

_Captured: 2017-07-30 at 15:53 from [www.suppertime.co.uk](http://www.suppertime.co.uk/blogmywiki/2017/07/flotilla-radio/)_

![](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2017/07/flotilla-radio-icon-1024x682.jpg)

> _flotilla radio_

As you may know, [I love making different internet radios with Raspberry Pis](http://www.suppertime.co.uk/blogmywiki/piradio/)! This week [I've been rediscovering the Pimoroni Flotilla modular physical computing devices](http://www.suppertime.co.uk/blogmywiki/2017/07/flotilla/) which I backed on Kickstarter a few years ago, and as my first Python project with Flotilla it made sense to… make a radio with lovely controls.

Here's what I used:

  * A Raspberry Pi 3 with updated Jesse Raspbian installed and an internet connection
  * A TV as a display and audio output (you can use powered speakers or headphones just as easily for the audio output).
  * A Pimoroni Flotilla Dock, Touch buttons, Slider, 8×8 Matrix display and rotary Dial - though you could do a bare bones version with just the Touch buttons.

First up I had to install mpc and mpd which I use to play radio streams:

`sudo apt-get install mpc mpd`

I had lot of problems on this new Pi with mpc & mpd hanging when I changed channels a few times - something I'd not experienced previously making Raspberry Pi radios with older versions of Raspbian. Here's how to fix this: first open the mpd config file with nano like this:  
`sudo nano /etc/mpd.conf`

Then edit these lines to remove some # signs (uncomment) and change the mixer_type from hardware to software so it looks like this:

`audio_output {  
type "alsa"  
name "My ALSA Device"  
device "hw:0,0" # optional  
mixer_type "software" # optional  
mixer_device "default" # optional  
mixer_control "PCM" # optional  
mixer_index "0" # optional  
}`

Now add some radio station URLs using the `mpc add` command. I added Radio 1, BBC World Service News, FIP and Radio 4. For example to add FIP I typed  
`mpc add http://chai5she.cdn.dvmr.fr/fip-midfi.mp3`

You can find BBC radio URLs on [my big list here](http://www.suppertime.co.uk/blogmywiki/2015/04/updated-list-of-bbc-network-radio-urls/).

You need 4 stations only as you only have 4 buttons for presets. They get added in order but you can check your list of presets by typing  
`mpc playlist`

And you can change the order using the move command, for example to move station 4 to preset 2 just type:  
`mpc move 4 2`

Then I wrote some Python code to talk to the Flotilla modules and play radio stations. Once I'd got mpc working properly the hardest thing was getting numbers on the Matrix display. I am very grateful to [veryalien for their help on the Pimoroni forum](http://forums.pimoroni.com/t/flotilla-python-display-text-on-matrix-module/5358) getting this to work.

![](http://www.suppertime.co.uk/blogmywiki/wp-content/uploads/2017/07/radio-icon-1024x682.jpg)

I made the radio graphic by sketching it out on graph paper and converting each row to binary (bottom row first!) then hexadecimal and added it to the list that contains the font for digits 1-4 as pinched from the Pimoroni javascript code for Rockpool.

Before running any Python code with Flotilla you have to stop the Flotilla daemon from running on the Pi by typing the following command:  
`sudo service flotillad stop`

Then plug in your Flotilla modules and run the Python code below. You should see a little radio icon appear on the Matrix display to let you know it's working. The slider adjusts the display brightness, the rotary Dial adjusts the volume, the Matrix display shows a number 1-4 to let you know which preset is selected (though you could easily have scrolling text with the station name - see the Pimoroni forum for details). Ctrl-c on the keyboard will stop the radio, clear the display and exit the script.

Happy listening!
    
    
    #!/usr/bin/env python
    
    # simple internet radio
    # Script by Giles Booth x
    # adapted from motor control script by Tanya Fish
    # www.suppertime.co.uk/blogmywiki
    # stop flotilla daemon before running Python with Flotilla
    
    import os
    import sys
    import flotilla
    
    # radio logo and font for digits 1-4
    digits = [
        [0xff,0x81,0xad,0x81,0xff,0x02,0x04,0x08],
        [0x00,0xfc,0x30,0x30,0x30,0x30,0x70,0x30],
        [0x00,0xfc,0xcc,0x60,0x38,0x0c,0xcc,0x78],
        [0x00,0x78,0xcc,0x0c,0x38,0x0c,0xcc,0x78],
        [0x00,0x1e,0x0c,0xfe,0xcc,0x6c,0x3c,0x1c]
        ]
    
    # Looks for the dock, and all of the modules we need
    # attached to the dock so we can talk to them.
    
    dock = flotilla.Client()
    print("Client connected...")
    
    while not dock.ready:
        pass
    
    print("Finding modules...")
    touch = dock.first(flotilla.Touch)
    matrix = dock.first(flotilla.Matrix)
    dial = dock.first(flotilla.Dial)
    slider = dock.first(flotilla.Slider)
    
    if touch is None or matrix is None or dial is None or slider is None:
        print("Some modules required were not found...")
        dock.stop()
        sys.exit(1)
    else:
        print("Found. Running...")
    
    os.system("mpc load")
    dial_val = 0
    
    # set initial brightness and radio logo
    brightness = max(int((slider.position/1023.0)*100.0),1)
    matrix.clear()
    matrix.set_brightness(brightness)
    for row in range(0, 8):
        for col in range(0, 8):
            if digits[0][row] & (1 << col):
                matrix.set_pixel(col, 7-row, 1)
    matrix.update()
    
    # Starts the loop going so it keeps working until we stop it
    try:
        while True:
    
            new_brightness = max(int((slider.position/1023.0)*100.0),1)
            if new_brightness != brightness:
                brightness = new_brightness
                matrix.set_brightness(brightness)
                matrix.update()
    
    # volume control using dial
            new_dial_val = int(float(dial.data[0])/10.23)
            if new_dial_val != dial_val:
                dial_val = new_dial_val
                os.system("mpc volume " + str(dial_val))
    
    # Looks for a Touch module and listens for an input
    
            if touch.one:
                os.system("mpc play 1")
                matrix.clear()
                for row in range(0, 8):
                    for col in range(0, 8):
                        if digits[1][row] & (1 << col):
                            matrix.set_pixel(col, 7-row, 1)
                matrix.update()
    
            if touch.two:
                os.system("mpc play 2")
                matrix.clear()
                for row in range(0, 8):
                    for col in range(0, 8):
                        if digits[2][row] & (1 << col):
                            matrix.set_pixel(col, 7-row, 1)
                matrix.update()
    
            if touch.three:
                os.system("mpc play 3")
                matrix.clear()
                for row in range(0, 8):
                    for col in range(0, 8):
                        if digits[3][row] & (1 << col):
                            matrix.set_pixel(col, 7-row, 1)
                matrix.update()
    
            if touch.four:
                os.system("mpc play 4")
                matrix.clear()
                for row in range(0, 8):
                    for col in range(0, 8):
                        if digits[4][row] & (1 << col):
                            matrix.set_pixel(col, 7-row, 1)
                matrix.update()
    
    # This listens for a keyboard interrupt, which is Ctrl+C and can stop the program
    except KeyboardInterrupt:
        os.system("mpc stop")
        matrix.clear()
        matrix.update()
        print("Stopping Flotilla...")
        dock.stop()
