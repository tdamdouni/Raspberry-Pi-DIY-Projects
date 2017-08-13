# Detect Motion With OpenCV, No PIR Sensor Needed

_Captured: 2017-08-09 at 18:28 from [www.hackster.io](https://www.hackster.io/brendan-lewis/detect-motion-with-opencv-no-pir-sensor-needed-bbeacf)_

![Detect Motion With OpenCV, No PIR Sensor Needed](https://hackster.imgix.net/uploads/attachments/301078/opencv_logo_WWl0EKPASl.png?auto=compress%2Cformat&w=900&h=675&fit=min)

When you have HATs connected to your Pi, you cannot connect a PIR sensor to measure motion. But don't worry! There is an alternative: OpenCV and a Camera Module. This project will show how to set up a Pi and a Camera Module to detect motion, and even save a picture of what was moving!

**Please contact me or comment on the bottom of this page if you have any problems with this project.**

I recommend to read through the instructions to make sure you have enough time to install OpenCV. Make sure you have Python 2.7 installed on your Pi. Also, make sure your Pi has a steady Internet connection for the entire setup and after.

If you followed that, you're good to go!

> Note: the guide in steps 2, 3, and 4 is modified from the tutorial at [this site](http://www.pyimagesearch.com/2016/04/18/install-guide-raspberry-pi-3-raspbian-jessie-opencv-3/).

To get started, open a terminal. The commands that follow are to be typed here.

First, you can optionally purge the Wolfram Engine to free up a lot of data:
    
    
    sudo apt-get purge wolfram-engine
    

Now, run the following commands in order separately:
    
    
    sudo apt-get update
    sudo apt-get install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev
    sudo apt-get install -y libjasper-dev libpng12-dev libavcodec-dev libavformat-dev
    sudo apt-get install -y libswscale-dev libv4l-dev libxvidcore-dev libx264-dev
    sudo apt-get install -y libgtk2.0-dev libatlas-base-dev gfortran
    sudo apt-get install -y python2.7-dev python3-dev
    cd ~
    

(Note: the next few commands uses OpenCV version 3.1.0, but you can use a different version number if you prefer. Make sure the version numbers are the same in the URL, however.)
    
    
    wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
    unzip opencv.zip
    wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
    unzip opencv_contrib.zip
    sudo mv opencv-3.1.0 opencv
    sudo mv opencv_contrib-3.1.0 opencv_contrib
    

(Note: if you already have pip installed, you can skip the next command.)
    
    
    sudo apt-get install -y python-pip
    

(Note: the following command takes a very long time to execute. If you think it's stuck, just wait another 10-20 minutes and it should be fine.)
    
    
    sudo pip install numpy
    

Good job! You have... wait, all that just to get ready?!?! Don't worry, just 3-4 more hours of waiting for OpenCV to install... :(

Just keep typing commands in the terminal window you have up:
    
    
    cd opencv
    mkdir build
    cd build
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..
    

(Note: make sure you remember the two periods at the end of the above command. They are not separated by a space or any other character between themselves.)
    
    
    make -j4
    

(Note: if the above command results in an error, just type "make clean" and then "make". This will take a few hours using either command however, so you can go watch a movie or something right now.)
    
    
    sudo make install
    sudo ldconfig
    

Alright! OpenCV is now installed! Don't pop the champagne yet... we have to make sure it works!

Type the following into the terminal:
    
    
    python
    

(Note: you should see a ">>> " prompt.)
    
    
    import cv2
    print(cv2.__version__)
    exit()
    

If you see "3.1.0" or whatever version number you put in earlier, great! If Python prints out an error, put it in the comments section of this page or send me a message, and I will try to help.

Finally, to save space, type the following once you are **completely sure** OpenCV is installed:
    
    
    cd ~
    rm -rf opencv opencv_contrib
    

Finally! Hooray! Wait... we're still not done? :0

OpenCV is a very powerful tool. It can do many useful tasks all by itself, such as facial recognition. But in this project, I am only going to show you a rudimentary way how to detect motion. To get started, type this in your terminal:
    
    
    cd ~
    wget -O opencv_motion.zip "https://github.com/blewis14/blewis14-raspi-code/blob/master/pi-opencv-code.zip?raw=true"
    

(Note: the "wget" command is two lines long on hackster.io, but it should be one line in your terminal.)
    
    
    unzip opencv_motion.zip
    sudo rm opencv_motion.zip
    

The code should now be loaded on your Pi.

To complete setting up, you will need to follow Steps 1 and 2 of [this project here](https://www.hackster.io/brendan-lewis/weather-monitor-13f9ce), or use your Dropbox access token if you have one already. Type the following in the terminal:
    
    
    cd opencv_motion
    sudo nano pi_surveillance.py
    

Now, where it says to put the access token, there will be a string that looks like "YOUR_TOKEN_HERE". Delete the part between the double quotes and replace it with your access token. Press Ctrl+O (to save) and then Ctrl+X (to quit).

Usually, you will want to run this program automatically on boot. To do that, type this in your terminal:
    
    
    crontab -e
    

If you have never used crontab before, you will have to select which editor you want to use. Type the number next to "nano" and press Enter. Scroll down to the end of the crontab by using the arrow keys, and on a new line, type this:
    
    
    @reboot sudo python ~/opencv_motion/pi_surveillance.py &
    

Good job! You are done with the software setup.

To finish, turn the Pi off and plug the Camera Module into the Pi.

All that is left is to put it in a cool-looking case and put it wherever you want! Just make sure water can't get into the case or the area where it is located.

Once it is in your favorite spot, turn it on and it should automatically work!

Wow! That was fun! Anything I can do now? Maybe a [Weather Monitor](https://www.hackster.io/brendan-lewis/weather-monitor-13f9ce) can compliment its abilities...
    
    
    warnings.filterwarnings("ignore")
    
    db = dbx.Dropbox("YOUR_TOKEN_HERE")
    
    camera.resolution = (640,480)
    camera.framerate = 16
    rawCapture = PiRGBArray(camera, size=(640,480))
    
    time.sleep(2.5)
    lastUploaded = datetime.datetime.now()
    
    for f in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    	frame = f.array
    	timestamp = datetime.datetime.now()
    
    	frame = imutils.resize(frame, width=500)
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    		avg = gray.copy().astype("float")
    		rawCapture.truncate(0)
    
    	cv2.accumulateWeighted(gray, avg, 0.5)
    	frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
    
    	thresh = cv2.threshold(frameDelta, 5, 255,
    	thresh = cv2.dilate(thresh, None, iterations=2)
    	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    
    	for c in cnts:
    		if cv2.contourArea(c) < 5000:
    
    		(x, y, w, h) = cv2.boundingRect(c)
    		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    	ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    	cv2.putText(frame, "{}".format(ts), (10, 20),
    		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    	if text == "!":
    		if (timestamp - lastUploaded).seconds >= 3.0:
    
    			if motionCounter >= 8:
    				cv2.imwrite(t.path, frame)
    				print "[UPLOAD] {}".format(ts)
    				path = "{base_path}/{timestamp}.jpg".format(base_path="/", timestamp=ts)
    				client.put_file(open(t.path, "rb").read(), path)
    				
    
    
    	rawCapture.truncate(0)
    
