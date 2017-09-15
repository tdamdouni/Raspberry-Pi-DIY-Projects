# Keeping an eye on a website with rpi0 and Scroll pHAT HD

_Captured: 2017-09-01 at 12:23 from [forums.pimoroni.com](http://forums.pimoroni.com/t/keeping-an-eye-on-a-website-with-rpi0-and-scroll-phat-hd/4487)_

I just finished my first rpi project and I wanted to share it. I made a clock that works as usual until a production website runs into problems. Then intead of showing time, it blinks continuously to draw my attention to the problem. The website uses "normal.css" if everything is ok and "hot.css" if there is a problem. So the clock looks at the name of the css file the website is using and acts accordingly.

I don't know much python so I recyled example code. Improvements or comments are welcome. Here is the /home/pi/clock.py I created:
    
    
    #!/usr/bin/env python
    
    import os
    import time
    import signal
    import math
    import scrollphathd
    from scrollphathd.fonts import font3x5
    
    def warning():
            speed_factor = 10
            scale = (math.sin(time.time() * speed_factor) + 1) / 2
            offset = 0
            for x in range(scrollphathd.width):
                for y in range(scrollphathd.height):
                    offset += 1
                    color = 0.85 * scale * (offset % 2)
                    scrollphathd.pixel(x, y, color)
            scrollphathd.show()
    
    def clock():
            scrollphathd.rotate(180)
            scrollphathd.clear()
            str1 = time.strftime("%H%M") 
            scrollphathd.write_string(str1, x=1, y=1, font=font3x5, brightness=0.01)
            scrollphathd.show()
            time.sleep(0.1)
    
    while True:
            web = os.popen("curl -s https://example.com | grep .css").read()
            t_end = time.time() + 60 * 1
            if "hot.css" in web:
                    while time.time() < t_end:
                            warning()
            else:
                    while time.time() < t_end:
                            clock()

After this I created a cron job to make sure that the script above is running and to restart it if it is not working. Since the only python program running in this rpi0 is the above clock script, the restart script simply looks if any python program is running and if there is none, restarts the clock script. Here is /home/pi/restart.sh I created:
    
    
    #!/bin/bash
    
    if [ "$(pidof python)" ]
    then
      exit
    else
      nohup /home/pi/clock.py &>/dev/null &
    fi

Now

`crontab -e`

and add the line:

`* * * * * /home/pi/restart.sh`

That's all.

I was not happy with the look of the font so I changed it a bit as well, see the [forum_post5](http://forums.pimoroni.com/t/scroll-phat-hd-3x5-font-change/4485) about it.

Cheers.

  


os time signal math scrollphathd scrollphathd.fonts font3x5 speed_factor = scale = (math.sin(time.time() * speed_factor) + ) / offset = x range(scrollphathd.width): y range(scrollphathd.height): offset += color = * scale * (offset % ) scrollphathd.pixel(x, y, color) scrollphathd.show() scrollphathd.rotate() scrollphathd.clear() str1 = time.strftime() scrollphathd.write_string(str1, x=, y=, font=font3x5, brightness=) scrollphathd.show() time.sleep() : web = os.popen().read() t_end = time.time() + * web: time.time() < t_end: warning() : time.time() < t_end: clock()
