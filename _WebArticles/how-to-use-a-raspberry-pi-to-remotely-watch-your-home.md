# How to use a Raspberry Pi to remotely watch your home

_Captured: 2017-08-31 at 01:00 from [www.techradar.com](http://www.techradar.com/how-to/computing/use-a-raspberry-pi-to-remotely-watch-your-home-1314466)_

![](http://cdn.mos.cms.futurecdn.net/3a64eb022f200e4d94a141e1b5a54c96-970-80.jpg)

For this Raspberry Pi project we'll create a remote monitor for tracking activity in a home. Before we begin, make sure that your webcam is plugged into your Raspberry Pi. To update our system and install the webcam motion software, you'll need to open XTerminal and type:

**$ sudo apt-get update && sudo apt-get install motion**

With motion installed let's configure it with:

**$ sudo nano /etc/default/motion**

You'll see **start_motion_daemon=no** change this to **yes**.

Now press Ctrl+o to save and Ctrl+x to quit. Now we need to make a few changes to our motion.conf file. Open it with **$ sudo nano /etc/motion/motion.conf** . Ensure the following is correct before saving (Ctrl+o) and exiting (CtrlL+x) nano

**daemon on**

**width 640**

**height 480**

**framerate 100**

**stream_localhost off**

Reboot your Raspberry Pi before continuing. Now let's test our stream. In a terminal type **$ sudo service motion start .**

Now in a browser on another machine type in the IP address of your Raspberry Pi, you can find this in the terminal by typing hostname -I followed by :8081 so for example my IP address was 192.168.0.3:8081.

You should now see a video stream in your browser. Now that we have the stream working let's embed it into a live web page. To do this we will need to install Apache. In a terminal type** $ sudo apt-get install apache2 -y** . This will also create a new directory in /var/ called /www/ which we shall use to serve our pages.

Open the text editor on your Raspberry Pi. We will now write a few lines of HTML to build a simple web page.

**Puppy/Baby Monitor**

**## I wonder what the dog/baby is up to?**

**src="http://192.168.0.3:8081/">**

**script>**

We start by declaring the document as a valid HTML document and give the page a title to identify it in our browser. Now we move to the where we use a framework called strapdown, which mixes markdown - a popular writing format - with Twitter's bootstrap framework.

In essence we can make a nice page rather quickly. We're using the cyborg style as it's dark and looks great on devices. To create a headline we use two hashes (#) and then type the contents of the headline. Next, we add an image whose source is the IP address of the webcam stream.

To make sure the IP address matches that of your Pi we add :8081 at the end. We then instruct the browser to load a JavaScript file containing the strapdown functionality. Save your file as index.html to your home directory. Open a terminal and type the following to copy the file to our web server:

**$ sudo cp /home/pi/index.html /var/www/html/**

Finally, we need to start our web server and restart the motion service.

**$ sudo service apache2 start**

**$ sudo service motion restart**

Now visit your Raspberry Pi's IP address - you no longer need to add :8081 to the end of the IP) - and you will now see a video stream from your Raspberry Pi.

The Raspberry Pi has made many different types of projects possible and one that's popular is CCTV. The official Raspberry Pi Camera, along with the Pi offer a low cost, high quality and low-power project you can build quickly.

In this project, we used motion to stream our webcam to a webpage, but motion can be used to search for motion and stream as well, eg we can record a video stream to a local or cloud device which will be triggered by a burglar, baby or Jack Russell terrier.

Add a Passive Infra Red (PIR) sensor to this code, such as the one used in our delivery watch project, and you have a powerful application that can alert you to incidents and record the evidence. Another great application to use with a webcam is [Zoneminder](http://www.zoneminder.com) which also works with the Raspberry Pi.

Using Zoneminder, you'll be able to monitor multiple streams and set up zones which will trigger an alert, eg a zone drawn around a door frame would trigger if a person used the door, but the surrounding area wouldn't be monitored for activity.
