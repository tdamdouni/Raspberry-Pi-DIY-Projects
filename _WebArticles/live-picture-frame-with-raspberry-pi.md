# Live Picture Frame With Raspberry PI

_Captured: 2017-11-29 at 09:40 from [www.instructables.com](http://www.instructables.com/id/Live-Picture-Frame-With-Raspberry-PI/)_

![](https://cdn.instructables.com/FQR/VK48/JACTYDGK/FQRVK48JACTYDGK.ANIMATED.MEDIUM.gif)

![](https://cdn.instructables.com/FAQ/09I6/JACTYDBC/FAQ09I6JACTYDBC.SMALL.jpg)

![](https://cdn.instructables.com/FJ5/36U0/JACTYDCL/FJ536U0JACTYDCL.SMALL.jpg)

I recently moved from UK back to Spain to work remotely, and since then, I've been curious about how the weather is there, specially when talking with people on the other country. Is it raining today ? Is the sun gone already ?

To address that problem, I found a few live videos/webcams about london like [earthtv](http://www.earthtv.com/en/webcam/london-millennium-bridge) or [London Tower Bridge](https://www.youtube.com/watch?v=SMOb9d9s_mI) so I kept those videos on one of the tabs of my browser.

But, wouldn't be cool to have it on a separate picture frame, always there, just like a normal picture, but live.

That's why I built a slim picture frame from old recycled components. To see the Tower Bridge at day and at night.

## Step 1: Materials

These are the materials I used to create the live picture. All these items were already on my inventory:

  * Old ultra-thin LCD screen from a broken laptop (10 years old) 
  * 12v LCD controller board with VGA output 
  * Raspberry PI Zero 
  * HDMI to VGA adaptor 
  * 12v to 5v converter regulator 
  * Ikea [KNOPPANG](http://www.ikea.com/us/en/catalog/products/00297440) picture frame for A4 
  * Sonoff wireless switch (optional) 
  * VGA cable, micro usb cable, 12v splitter cable

## Step 2: Adjusting the Picture Frame

![](https://cdn.instructables.com/FQY/XPOS/JACTYDBB/FQYXPOSJACTYDBB.MEDIUM.jpg)

![](https://cdn.instructables.com/FWS/U7DC/JACTYDDS/FWSU7DCJACTYDDS.SMALL.jpg)

![](https://cdn.instructables.com/FCJ/AN87/JACTYDDR/FCJAN87JACTYDDR.SMALL.jpg)

The Ikea picture frame was made for A4 pictures, however, my 15'' LCD screen is slightly bigger than that, therefore we need to make some adjustments, first, increasing the hole in the white inner frame to 15''.

Then, cutting the back of the frame to the same size

Everything should fit together, so you should be able to see all the screen inside the inner frame

## Step 3: LCD Screen

![](https://cdn.instructables.com/FID/SCHZ/JACTYDIX/FIDSCHZJACTYDIX.MEDIUM.jpg)

![](https://cdn.instructables.com/FTB/9DJY/JACTYDA7/FTB9DJYJACTYDA7.SMALL.jpg)

![](https://cdn.instructables.com/F2H/IBPN/JACTYD90/F2HIBPNJACTYD90.SMALL.jpg)

![](https://cdn.instructables.com/F8A/8HN7/JACTYD91/F8A8HN7JACTYD91.SMALL.jpg)

Since a few years ago, I had an ultra thin LCD screen from an old broken laptop. After finding and using a controller board, I've been able to use it as extra screen for my desktop computer sugin a VGA connection.

Controller boards are specific to the LCD screen, you need to use an specific model for the serial number of your screen, you can find it on the back. Then it's a matter of searching ebay/aliexpress for a controller board listing compatibility with your screen model.

So I decided to recycle this screen now to create the canvas, because it's thin and lightweight.

I removed the front case, but left the back side to protect the screen, isolate the components and glue the cables and raspberry pi to it.

The Raspberry PI zero, glued to the back of the screen, is powered by the same power adaptor that powers the LCD screen, using a 12v to 5v conversor. So we don't need another extra cable connected into the screen. This is how it looks from the back.

## Step 4: Wall Mounting

![](https://cdn.instructables.com/FGY/17BQ/JACTYDOA/FGY17BQJACTYDOA.MEDIUM.jpg)

![](https://cdn.instructables.com/FD8/I9IB/JACTYDF5/FD8I9IBJACTYDF5.MEDIUM.jpg)

After everything has been assembled together, and tested, we're ready to hang it into the wall. For this I've just added two L shape hooks into the wall, and another two round hooks screwed into the plastic back of the screen.

After hanging it to the wall, I connected the 12v cable, and try to hide it using white tape.

## Step 5: Automatically Schedule Screen

![](https://cdn.instructables.com/FKQ/ENO6/JACTYDN1/FKQENO6JACTYDN1.MEDIUM.jpg)

![](https://cdn.instructables.com/FPV/W9X7/JACTYDK8/FPVW9X7JACTYDK8.SMALL.jpg)

![](https://cdn.instructables.com/F94/D621/JACTYDKD/F94D621JACTYDKD.SMALL.jpg)

![](https://cdn.instructables.com/F85/4R9G/JACTYDLS/F854R9GJACTYDLS.SMALL.jpg)

I'd like to schedule the frame, so it runs from 10AM to 7PM on weekdays, my working hours, so I can see London while I work remotely.

My first approach was to add some scripts on the Raspberry PI (cronjobs) to automatically switch ON/OFF the video output using `tvservice --off` or `xset dpms force off` however it didn't work pretty well in my case, because my LCD controller was not going into standby after turning off the HDMI signal.

So I decided to use a cheap wireless smart switch I've been using for a while, which can be scheduled and controlled by the phone, called [Sonoff](http://sonoff.itead.cc/en/). You could be using an [Energenie](https://coconauts.net/blog/2016/04/15/energinie-and-raspberry-pi-setup/), Xiaomi or something similar if you like.

This device needs to be connected in between your power cable, then you can configure it via the phone app.

Then you can add the schedule so the Sonoff, and the Raspberry PI and the screen will be turned ON and OFF automatically.

## Step 6: Software

![](https://cdn.instructables.com/FO5/N00A/JACTYDHO/FO5N00AJACTYDHO.MEDIUM.jpg)

Because I have now a Raspberry PI powered LCD screen hanging in the wall, I can pretty much display whatever I want. Like for example:

  * Web page using chrome `_chromium-browser --kiosk $url_` 
  * Video using omxplayer `_omxplayer video.mp4_` 
  * Use Kodi to display videos or other plugins. 
  * Youtube, twitch live video using the Livestreamer 
  * etc.

### Display live video using livestreamer

For this project, I chose to display the London Tower Bridge from a live stream in youtube.

This can be easily achieved using [livestreamer](https://github.com/chrippa/livestreamer) open source app, which allow us to display any live content from Youtube, twitch, livestream, dailymotion, etc... into a local video player, without using a web browser.

This is the command I'm using to display a Youtube link using omxplayer on fullscreen.
    
    
    livestreamer $youtube_url 720p -n -p "omxplayer --no-osd --win '0 0 1280 800' "

  * **$youtube_url** is a variable with the url of the livestream on youtube 
  * **720** is to select the resolution of the video, you can also use best or worst. 
  * **-n** or **\--fifo** Make the player read the stream through a named pipe instead of the stdin pipe 
  * **-p** player to use 
  * **\--no-osd** hide the UI from omxplayer 
  * **\--win** display video on full screen (my screen resolution) on omxplayer

[Omxplayer](https://github.com/popcornmix/omxplayer) is the best open source video player on Raspberry PI, you could try using VLC, but it will not work or display anything because of the lack of native hardware acceleration on Raspberry PI.

###  Script to display on startup 

I wanted to automatically run the video on startup, without any manual interaction.

There are a few ways to do it, but the best I found is using the `autostart` script located in _/home/pi/.config/lxsession/LXDE-pi/autostart_. On this script, you need to add `@` before every command.

If you want to keep the display ON, you'll need to add these lines to prevent the screen going OFF after a few minutes.
    
    
    @xset s off
    @xset -dpms
    @xset s noblank 

Then you can add the command from before to start the livestream on startup. This is all you need to add into the `/home/pi/.config/lxsession/LXDE-pi/autostart` script:
    
    
     @xset s off
    @xset -dpms
    @xset s noblank
    @livestreamer <a href="https://youtu.be/SMOb9d9s_mI" rel="nofollow"> https://youtu.be/SMOb9d9s_mI </a> 720p -n -p "omxplayer --no-osd --win '0 0 1280 800' " 

## Step 7: Conclussions and Improvements

This was an easy and cheap project to build, if you have an old screen, or you get a cheap one. The picture frame looks very nice hanging on the wall, and thanks to youtube and livestreamer, we can display any video very easily.

It took me some time to find the best streaming combination on Raspberry PI Zero. I tried using `_chromium-browser --kiosk_` but after sometime the browser was crashing; I tried using VLC to display M3U8 streaming video, but VLC was not efficient enough. Some links did not play on omxplayer, so at the end, I decided to use livestreamer, which works pretty well, and you can use it with other sources too.

I'd like to have a better LCD screen, maybe LED, with a direct HDMI connection and better viewing angle.

You could use the spare 12v connector to add a LED strip on the back of the frame, if you want to have some extra light effect.

Let me know what you think about this project, and if you've built your own.

## Comments
