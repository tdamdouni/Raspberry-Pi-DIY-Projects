# Raspberry Pi: Wall Mounted Calender and Notification Center

_Captured: 2016-01-10 at 02:44 from [m.instructables.com](http://m.instructables.com/id/Raspberry-Pi-Wall-Mounted-Calender-and-Notificatio/?ALLSTEPS)_

[ ![Picture of Raspberry Pi: Wall Mounted Calender and Notification Center](http://cdn.instructables.com/FGM/NT5I/IIVZRAIE/FGMNT5IIIVZRAIE.MEDIUM.jpg) ](http://www.instructables.com/file/FGMNT5IIIVZRAIE/)

> _[Picture of Raspberry Pi: Wall Mounted Calender and Notification Center](http://www.instructables.com/file/FGMNT5IIIVZRAIE/)_



![Raspberry Pi: Wall Mounted Calender and Notification Center](http://cdn.instructables.com/FGM/NT5I/IIVZRAIE/FGMNT5IIIVZRAIE.SQUARE2.jpg)

#### Intro: Raspberry Pi: Wall Mounted Calender and Notification Center

Before the "digital age" many families used wall calendars to show a monthly view of upcoming events. This modern version of the wall mounted calendar includes the same ...

1 

![The Hardware](http://cdn.instructables.com/FNO/EQMC/IIVZRAIF/FNOEQMCIIVZRAIF.SQUARE2.jpg)

#### Step 1: The Hardware

This is the hardware setup. Find a LCD laptop screen . Order a controller board on Ebay. Search for LCD Controller Driver Board and the serial number of ...

2 

#### Step 2: The Software

The setup is somehow turning the Raspberry Pi into a kiosk. The OS will auto start a website in full screen mode,and the Push Buttons is used to ...

3 

![Create a webpage and webserver](http://www.instructables.com/static/defaultIMG/default.SQUARE2.png)

#### Step 3: Create a webpage and webserver

The webpage is the canvas the Raspberry Pi will display. The canvas can be filled with any information. I will show you how i to embed a google ...

4 

![Install a web browser and customize the calendar design](http://www.instructables.com/static/defaultIMG/default.SQUARE2.png)

#### Step 4: Install a web browser and customize the calendar design

There a many web browser out there. But I have only find one that can handle these three requirements; 1) can handle the modern version of google calendar, ...

5 

![Set up the Push Buttons](http://www.instructables.com/static/defaultIMG/default.SQUARE2.png)

#### Step 5: Set up the Push Buttons

The Push Buttons is used to browse forward and backwards in the calendar month view. By default this is done by pressing "p" and "n" at a keyboard. ...

[ ![Picture of Raspberry Pi: Wall Mounted Calender and Notification Center](http://cdn.instructables.com/FGM/NT5I/IIVZRAIE/FGMNT5IIIVZRAIE.MEDIUM.jpg) ](/file/FGMNT5IIIVZRAIE/)

Show All Items  
__

Before the "digital age" many families used wall calendars to show a monthly view of upcoming events. This modern version of the wall mounted calendar includes the same basic functions:

  * A monthly agenda 
  * Sync of family members activities 
  * Easy browse between months

Beyond those basic functions this gadget will also handle:

  * A whether forecast 
  * Upcoming events in the surrounding area 
  * Live information about the public transport 
  * And even more... 

What you need:

  * Raspberry Pi 2 
  * USB Wifi Dongle. (Like Edimax 150Mbps Wireless nano ) 
  * LCD laptop screen (take one from a broken laptop [ http://www.instructables.com/id/Old-laptop-screen...](http://www.instructables.com/id/Old-laptop-screen...)
  * Controller card for the laptop screen (search Ebay for LCD Controller Driver Board and the serial number of your laptop screen) 
  * Some Push Button Switches (Like [http://www.ebay.com/itm/16mm-Start-Horn-Button-Mom...](http://www.ebay.com/itm/16mm-Start-Horn-Button-Momentary-Stainless-Steel-Metal-Push-Button-Switch-2Y-/281773241529?hash=item419afe74b9:g:TQ8AAOSwLVZVzbVg) ) 
  * Webserver running a custom made homepage 
  * Piece of wood. Height should be more than 30mm, so the electronics can fit inside. The width and height depends on the size of your laptop screen. 
  * Sheet of cork. (Like this [ http://www.pandurohobby.se/Katalog/50-Skapa-Dekor...](http://www.pandurohobby.se/Katalog/50-Skapa-Dekor...)
  * Short HDMI cable 
  * Powersuply for controller board and Raspberry Pi. 
  * Foamcore 
  * Glue. 
  * Mounting screws .

(Inspired by the instructable by Piney [http://www.instructables.com/id/Raspberry-Pi-Wall-...](http://www.instructables.com/id/Raspberry-Pi-Wall-Mounted-Google-Calendar/))

## Step 1: The Hardware

[ ![Picture of The Hardware](http://cdn.instructables.com/FNO/EQMC/IIVZRAIF/FNOEQMCIIVZRAIF.MEDIUM.jpg) ](/file/FNOEQMCIIVZRAIF/)

[ ![PC270027.JPG](/intl_static/img/pixel.png) ![PC270027.JPG](http://cdn.instructables.com/F2C/LZCD/IIVZRAIJ/F2CLZCDIIVZRAIJ.MEDIUM.jpg) ](/file/F2CLZCDIIVZRAIJ/)

[ ![PC270028.JPG](/intl_static/img/pixel.png) ![PC270028.JPG](http://cdn.instructables.com/F09/UYS5/IIVZRAK2/F09UYS5IIVZRAK2.MEDIUM.jpg) ](/file/F09UYS5IIVZRAK2/)

[ ![PC270030.JPG](/intl_static/img/pixel.png) ![PC270030.JPG](http://cdn.instructables.com/FUH/X7G7/IIVZRAK5/FUHX7G7IIVZRAK5.MEDIUM.jpg) ](/file/FUHX7G7IIVZRAK5/)

[ ![PC280031.JPG](/intl_static/img/pixel.png) ![PC280031.JPG](http://cdn.instructables.com/F3D/DZBD/IIVZRAKA/F3DDZBDIIVZRAKA.MEDIUM.jpg) ](/file/F3DDZBDIIVZRAKA/)

[ ![PC280032.JPG](/intl_static/img/pixel.png) ![PC280032.JPG](http://cdn.instructables.com/FYS/VOSE/IIVZRAKC/FYSVOSEIIVZRAKC.MEDIUM.jpg) ](/file/FYSVOSEIIVZRAKC/)

[ ![PC280036.JPG](/intl_static/img/pixel.png) ![PC280036.JPG](http://cdn.instructables.com/FLM/YX4C/IIVZRAID/FLMYX4CIIVZRAID.MEDIUM.jpg) ](/file/FLMYX4CIIVZRAID/)

[ ![PC280033.JPG](/intl_static/img/pixel.png) ![PC280033.JPG](http://cdn.instructables.com/F13/RRPN/IIVZRAKE/F13RRPNIIVZRAKE.MEDIUM.jpg) ](/file/F13RRPNIIVZRAKE/)

[ ![568706a9937ddb7eb300136f.jpeg](/intl_static/img/pixel.png) ![568706a9937ddb7eb300136f.jpeg](http://cdn.instructables.com/F7P/B21W/IIVZSCDU/F7PB21WIIVZSCDU.MEDIUM.jpg) __ ](/file/F7PB21WIIVZSCDU/)

Show All Items  
__

This is the hardware setup. 

  1. **Find a LCD laptop screen** . Order a controller board on Ebay. Search for LCD Controller Driver Board and the serial number of your laptop screen.  

Read more: [http://www.instructables.com/id/Old-laptop-screen-..](http://www.instructables.com/id/Old-laptop-screen-into-Monitor/)

  2. **Craft a piece of wood. **Height should be more than 30mm, so the electronics can fit inside. The width and height depends on the size of your laptop screen, have a margin for an extra 10 mm on all sides. Carve out and make room for the electronics on the back. Drill holes for the buttons and wires. 
  3. **Fasten the laptop screen**. I used the orginal mounting frame from the laptop. 
  4. **Cut out foamcore** with equal thickness as the screen. and glue it on the wooden slab. 
  5. **Cover all sides with cork**. Cut with a "snap-off blade knife" and glue with "glue spray". 
  6. **Mount the Push Buttons**. Use a large drill, and drill carefully by hand. 
  7. **Connect the electronics. **Connect three of the Push Buttons to GPIO-pins 19/20/21 and to ground. [ https://ms-iot.github.io/content/images/PinMappin...](https://ms-iot.github.io/content/images/PinMappings/RP2_Pinout.png) Find out the pin for On/Off button for the controller board, and connect it with the fourth Push Button. (You will find it by trying to connect ground to each pin, suddenly the LCD will light up). Finaly, connect the HDMI cable between Raspberry and controller board, and connect the screen to the controller board.

## Step 2: The Software

The setup is somehow turning the Raspberry Pi into a kiosk. The OS will auto start a website in full screen mode,  
and the Push Buttons is used to control the information at the website. The setup is:

  1. Install Raspbain on Raspberry Pi   

(<https://www.raspberrypi.org/documentation/installation/noobs.md>)  

  2. Sign up for a Google Calender. (<https://calendar.google.com>). Add your upcomming event. Ask for access to your family members calendar, or create a speceific "family calender" and give the rest of the familiy acess to it. Make your calendar more dynamic by adding external calenders. Facebook events, public holidays, and week number has been practical for me. More inspiration here: [http://lifehacker.com/the-coolest-things-you-can-a...  

](http://lifehacker.com/the-coolest-things-you-can-automatically-add-to-google-1562119291)

  3. Set up a webpage and a webserver  
  4. Install a web browser and customize the calendar design  
  5. Set up the push buttons

Continue reading for details about 3-5 .

## Step 3: Create a webpage and webserver

The webpage is the canvas the Raspberry Pi will display. The canvas can be filled with any information. I will show you how i to embed a google callender. The embeed code is generate by googles own aplication. This youtube shows how to get it to work: <https://www.youtube.com/watch?v=2tnYwbs-yDk>

Google Calendar have built in keyboard shortcuts. Press N and the next month will appear, press P and the previously month is shown. This will only work when the < iframe > is in focus. I have created a JavaScript that ensure that focus is correct. 

An example file of html code is attached (change name from index.html.txt to index.html). For privacy, I have replace some of the code with "*___REPLACED___*". Instead, use the embeed code generated by google.

Either put the index.html file on your own webhost, or turn your Raspberry Pi into a webserver and host it local. If you already have a webhost continue to the next step. Install a webserver by following this guide: [https://www.raspberrypi.org/documentation/remote-a...](https://www.raspberrypi.org/documentation/remote-access/web-server/apache.md) Now save your modifed index.html to /var/www/html/index.html, like this:

    
    
    sudo cp index.html /var/www/html/index.html

  * [ ![index.html.txt](http://www.instructables.com/static/defaultIMG/file/TXT.gif) index.html.txt ](/files/orig/FJM/0ICA/IIYZ0CV6/FJM0ICAIIYZ0CV6.txt)

## Step 4: Install a web browser and customize the calendar design

There a many web browser out there. But I have only find one that can handle these three requirements; 1) can handle the modern version of google calendar, 2) has a full screen mode, 3) can run a local CSS. The local CSS is used to change the appearances of the google calendar. The redesign can't be done at the webpage, because the CSS are embedded from another server (the google-server).

Install Iceweasel (Firefox for Linux)   
<https://www.youtube.com/watch?v=69fwZ8yMnz0>

Install this extension for Iceweasel:   
<https://addons.mozilla.org/en-US/firefox/addon/stylish/>

Open the "Stylish" extension tab in Iceweasel and customize the CSS to make the google callander look better. Se attached file i for an example.

Now, lets make Iceweasel to autostart and open your webpage at login. Type this in the Linux terminal:

    
    
    cd /home/pi//.config/autostart
    nano cal.desktop 

Write the following to the file. Change "localhost" to adress where your canvas-webpage are stored. Save and exit.

    
    
    [Desktop Entry]
    Type=Application
    Name=hemsida
    Exec=iceweasel localhost
    StartupNotify=false

  * [ ![stylish.css](http://www.instructables.com/static/defaultIMG/file.TINY.gif) stylish.css ](/files/orig/FCX/958L/IIXF7TGS/FCX958LIIXF7TGS.css)

## Step 5: Set up the Push Buttons

The Push Buttons is used to browse forward and backwards in the calendar month view. By default this is done by pressing "p" and "n" at a keyboard. Therefore the buttons will emulate those two keyboards commands. 

First, create a python script to make the push buttons work: [ http://razzpisampler.oreilly.com/ch07.html](http://razzpisampler.oreilly.com/ch07.html)

Download and install python-uinput, a python API to create virtual keyboards: [ http://tjjr.fi/sw/python-uinput/](http://tjjr.fi/sw/python-uinput/) Raspbian comes with both Python 2 and Python 3. Make sure you install uinput with the version you are using.

Put the uinput-API and the button script together. The final python scipt is attached.

Auto-start the python script on startup: [ http://www.instructables.com/id/Raspberry-Pi-Laun...](http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/.) Our launcher.sh will look like bellow. Replace "/home/pi/py_switch" to the path where you have stored the python script.

    
    
    cd /
    cd /home/pi/py_switch
    sudo modprobe uinput
    sudo python switch.py
    cd /
    

That's all!

  * [ ![switch.py](http://www.instructables.com/static/defaultIMG/file.TINY.gif) switch.py ](/files/orig/F56/WZI1/IIXF7UDF/F56WZI1IIXF7UDF.py)

<p>Can you tell me how you (auto-) login to google?</p><p>If the PI is rebooted, I need to relogin to google.com. Have you changed the sharing of the calender to public?</p><p>Thanks,</p><p>Frank</p>

<p>For those with mixed families (iOS and Android) like mine, we use an app called SquareHub that let's us add events in the app and then push them out to our iCal or Google Calendar. The App isn't amazing, but it is the only thing I could find that would allow us all to share events with each other. </p>

<p>Instead of push buttons could you salvage the touch pad from an otherwise broken laptop and mount that on the front?</p>

is RPi B+ ok for this?

<p>This should be a fine replacement. I/O wise they are almost identical(enough so for this). The main difference is you are going to have a slower experience... BUT. You are displaying a webpage, so you really don't need the extra power that comes from the B+. Hope this helps!</p>

<p>Sorry, I can't say. Google the difference and see if it have any effect for<br>the proposed functions. </p>

<p>I've never worked with Raspberry before, though from what I've read I don't think it would be too hard. One question: Can I set this up so that items I add to my iOS calendar or OS-X calendar be synced with this?</p>

<p>The easy way to do real-time calendar updates is to use a Google calendar. My wife and I share a &quot;family&quot; calendar which we update with family events.<br><br>This &quot;family&quot; Google Calendar is then displayed on a Raspberry Pi driven web page on a digital picture frame.</p><p>If your Google account has the calendar synced to your iPhone/iPad then any edits you make on your phone will appear in real time in the Google Calendar.</p>

I was just looking this up yesterday for a similar project. It is possible and there's a few good tutorials just a Google search away. 

<p>I'm new at this, is there a reason that you can't use a regular computer monitor? I know it'd be a bit thicker, but would it work?</p>

<p>Yeah it would work so long as it had a HDMI</p>

<p>The only thing I can think of to make this better is if it were running a version of Android (since iOS isn't open source) and you could use a touchscreen instead pf physical buttons. But at that point you could basically put a frame around a cheap tablet and mount it to the wall.</p>

<p>It's running Raspbian and using Google Calendar (which can sync with an iOS calendar). There's really no need for Android. They sell touch screens for the RasPi, but I think that could get expensive pretty quickly. Whether you could repurpose your own touch screen and get it to work with Raspbian, well, that's waaaay beyond my skill set.</p><p>But I do like your framed, wall-mounted tablet idea!</p>

<p>It's running Raspbian and using Google Calendar (which can sync with an iOS calendar). There's really no need for Android. They sell touch screens for the RasPi, but I think that could get expensive pretty quickly. Whether you could repurpose your own touch screen and get it to work with Raspbian, well, that's waaaay beyond my skill set.</p><p>But I do like your framed, wall-mounted tablet idea!</p>

<p>This is a brilliant idea/project and has got me shopping for the parts (additional to the rPI and 7&quot; screen which I already own) to build. I think rather than chopping around a wooden board, I will make something similar to a &quot;shadow box&quot; for mine. Will share some pictures when it's finished.</p>

<p>If it's a similar board as I've used and seen in the past, there may be 5v available from the connector above the 12v barrel connector on your controller board. You may be able to feed the pi from that and eliminate one plug. It looks great though, nicely done, I love the buttons you've added.</p>

<p>That's a good one! Thanks for the advice!</p>

<p>The index.html.txt downloads an empty file for me. Anyone else got that to work?</p>

<p>Great! I've been interested in setting up something along these lines for a long time. But too busy to spend the time to make something like this myself, I once thought, &quot;Surely someone must market such a product&quot;. And if so it should be cheaper to buy, since it would be a mass produced, than it would cost me in time and parts to make one for myself.&quot; So I scoured the Web for such a product on the consumer market. But to my dismay I found absolutely nothing of the kind out there. * Just I'm regularly dismayed that there isn't single a clock radio product that doubles as a stationary personal digital organizer (e.g. for setting up morning wake-up and reminder alarms months ahead of time, or customize wake-up alarm options to suit non-standard shift rotations for those who career choice makes the 5 day work week seem like a luxury everybody else takes for granted... example health care workers. But on that note,, the best clock radios today are of very disappointing quality compared to what one could buy in the way of these these appliances in less electronically advanced decades past, but I digress.) </p><p>*There is a product referred to as a digital whiteboard, for corporate office use, which has all the digital functionality of this wall mounted calendar/notification center, except it also sports interactive touch screen functionality. And it's insanely overpriced at many thousands of dollars a pop. Glad to see others here who are willing and able to do the work to make something just as practical for personal use, for a sensible fraction of the cost.</p>

<p>Great project. I'll be looking into doing this one. Thanks</p>

<p>This is great, especially if you can add to calendars of various family/household members. You could post reminders from home, via the calendar, for someone to &quot;get milk on way home&quot; or similar.</p>

Can I just pay you to make me one...

<p>Thanks for putting all this info together. Are you worried about the electronics getting hot? I bought a driver and hacked together a similar monitor without putting it in any enclosure yet. It seems like the board and especially the inverter get really hot even when they are not enclosed.</p><p>Also, where did you hide the power chords in your feature shot? </p>

If you think the electronics will get too warm, you could put heatsinks on the chips and put a fan in the enclosure. 

<p>This is very simple programming. I doubt any of the hardware would be taxed enough to make much heat. </p>

<p>Well, the electronics are a bit warm but not really hot. </p><p>The power supply comes from a hole on the back, and connects to the power plug for the fridge. (The blackish panel is the side cover for the fridge)</p>

<p>Awesome notification system. You can set up just about any kind of reminder that you can think of. </p>

__More Comments
