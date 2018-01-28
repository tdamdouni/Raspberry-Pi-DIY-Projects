# Raspberry Pi internet radio with web interface

_Captured: 2017-12-10 at 15:11 from [www.suppertime.co.uk](http://www.suppertime.co.uk/blogmywiki/2014/10/raspberry-pi-internet-radio-with-web-interface/)_

![Testing PiRadio](https://farm4.staticflickr.com/3943/15010648894_ce85be9c6a.jpg)

Having made [a bare-bones Raspberry Pi internet radio and one with an LCD display with push buttons to change channel](http://www.suppertime.co.uk/blogmywiki/piradio/), I decided that it would be nice to be able to control it from my smartphone, as well as displaying 'now playing' track information.

This was a fun challenge that kept me busy in the summer… I got distracted dreaming of different RaspberryPi shields (see below) with little speakers, buttons and LCD displays that would make nice Kickstarter projects, and I've been so busy since that I never wrote it up. So here, from memory and a few scribbled notes, is how you might do it…

![](https://farm4.staticflickr.com/3937/15651194202_3e5ff85288.jpg)

In brief, you install mpd and mpc music players, add some internet radio stations, install a simple web server and add a bit of PHP code to dish up a web page that controls the radio and displays tracklistings. It was the latter that was an especially tough nut to crack. The BBC, despite being funded from public subscriptions, does not seem to freely syndicate its 'now playing' data, and I have had to get it via a commercial third party's RSS feed (last.fm). Madness. (Or possibly The Specials. Without the now playing data, I'm not sure.) For my favourite radio station, fip, I used its Twitter feed to display the last 3 tracks played.

![](https://farm4.staticflickr.com/3944/15464254747_5e8c063a67.jpg)

![](https://farm4.staticflickr.com/3934/15464254577_3f2a999487.jpg)

**How to build one (very) roughly**

1) Start with a vanilla RaspberryPi running Raspbian OS 'headless' so it doesn't boot into a GUI. Adding wifi and giving it a static IP address is a good idea (in my experience, most wifi routers allow you to give devices the same IP address each time they start up). Enable SSH so you can log into your PiRadio remotely.

2) Install MPD and MPC music players as per <http://www.suppertime.co.uk/blogmywiki/piradio/>

3) Add internet radio stations of your choice as per <http://www.suppertime.co.uk/blogmywiki/piradio/>

4) Plug in some headphones, powered speakers or an amp into the analogue audio output of the RaspberryPi to test it works when you type  
`mpc play 1`

5) Optional: add a line to /etc/rc.local to play the radio station of your choice at boot-up.

6) Install nginx web server and PHP.

6.5) Install [SimplePie](http://simplepie.org/) to handle the RSS feeds that give 'now playing' data for BBC Radio.

7) Add my index.php and shutdown.php file **([code here](http://www.suppertime.co.uk/media/pi/pilittleradio.zip))** to /usr/share/nginx/www - there was probably a whole mess of permissions horror here that my notes glide over. It looks like I had fun making the shutdown work, I probably had to give the nginx user sudo rights or something horribly ill-advised.

8) You should now have a radio you (or your children! such hilarity!) can remotely control from a web-browser on any smartphone, computer, tablet - or indeed eBook reader. The stylesheet is optimised for an iPhone, but this easily be tweaked.

To do:  
\- enable recording (I did make some headway with this using streamripper but ran out of time).  
\- have a nice HTML5 volume control slider (this was beyond me).  
\- find a better way of setting it up so you can configure the wifi from a simple command line in a KanoOS-style.  
\- make it so you can easily edit the station list from web interface or command line.  
\- mesh in better with my Arduino-driven LCD display (at the moment if you change the channel using the web interface, the LCD shows the wrong station name).  
\- find someone to help me build my Kickstarter radio shield/widget. Adafruit do an LCD screen with buttons like my Arduino one, but it's a kit. I'd like a cute little box with a screen, buttons and a speaker or two, powered by USB.

![Controlling radio from Kindle](https://farm4.staticflickr.com/3863/14790916690_f8e8ec90f1.jpg)

_Controlling an early version of PiLittleRadio from an old Kindle 3G._
