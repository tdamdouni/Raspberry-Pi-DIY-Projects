# 5 Things You Can Do with the Raspberry Pi Camera Module

_Captured: 2017-05-06 at 16:21 from [www.makeuseof.com](http://www.makeuseof.com/tag/raspberry-pi-camera-module/)_

The flexibility of the Raspberry Pi knows no bounds, and just when you think you've achieved everything possible, something else comes along. This might be thanks to a great idea you or someone else had, or inspired by a newly released piece of expansion hardware for the device.

One of the first [expansions you should buy for the Raspberry Pi](http://www.makeuseof.com/tag/five-great-raspberry-pi-expansions-make-even-useful/) is the camera module. With a dedicated connector, the camera can be used for a variety of tasks. Let's take a look at them.

## First: Enable the Camera

Begin by making sure you have connected your Raspberry Pi camera to the mini-computer. Next, boot the device, and log in (we're assuming you're using the [default Raspberry Pi OS, Raspbian](http://www.makeuseof.com/tag/optimize-the-power-of-your-raspberry-pi-with-raspbian/)). At the command line, enter
    
    
    sudo raspi-config

In the menu select **Enable Camera**.

![muo-diy-picamera-enable](http://cdn.makeuseof.com/wp-content/uploads/2015/08/muo-diy-picamera-enable.png?x58476)

> _From here, select Enable, then Finish and Yes to reboot._

## Take A Photo

When your Pi restarts, login again, and at the prompt enter
    
    
    raspistill –o image.jpg

This will capture your first image, which you will be able to view in the GUI. If you're not already using Terminal from the GUI, you should switch to this, by using the command
    
    
    startx

Subsequent commands can be run in Terminal, and the results checked in the Raspbian file manager. You can take as many photos as you like with this command, although note that the filename, image.jpg, will need to be changed with each iteration of the command, to avoid overwriting the previous image.

Let's get a little more advanced, and instruct the Pi to take a timed photo following a single keypress.

Begin by installing the Python support for the camera.
    
    
    sudo apt-get install python-picamera python3-picamera

Once done, enter
    
    
    sudo idle &

This will start the Python environment. Python pops up regularly in Raspberry Pi tutorials, and is a surprisingly easy language to get to grips with. For more help with this, we suggest you check our [five best websites for learning Python](http://www.makeuseof.com/tag/5-websites-learn-python-programming/), and visit [Lynda.com if you're interested in taking your Python skills further](http://www.lynda.com/search?q=python).

Go to **File > New Window** to open a text editor and enter the following code:
    
    
    import time
    
    import picamera
    
    with picamera.PiCamera() as camera:
    
        camera.start_preview()
    
        time.sleep(0)
    
        camera.capture('/home/pi/Desktop/image.jpg')
    
        camera.stop_preview()

Use **File > Save** to save your work, naming it something like timedsnap.py. When you're ready to run the script, go to **Run > Run Module**, or just tap **F5**.

We can use this same script - with some modifications - to use the Raspberry Pi camera module for other projects.

## A PiCamera with a Timer

![muo-diy-picamera-device](http://cdn.makeuseof.com/wp-content/uploads/2015/08/muo-diy-picamera-device.jpg?x58476)

That same script can be reused with a small tweak to create a camera with a timed countdown, a huge benefit for any selfie-obsessed snappers. Let's face it, this is a Raspberry Pi, so you can probably find some way of mounting the case and camera on a selfie stick and go out in public with it.

To add a 5 second countdown, change the line
    
    
    time.sleep(0)

to
    
    
    time.sleep(5)

When you're done, remember to save and press F5 to begin the countdown. Say "Cheese!"

## Record Video with Your Raspberry Pi Camera

Taking stills is one thing, but what about video? Just as with a smartphone camera or standard desktop webcam (which is essentially what the Pi's camera is, just without the casing) you can record video too.

In the command prompt, modify the script as follows:
    
    
    import time
    
    import picamera
    
    
    
    with picamera.PiCamera() as camera:
    
        camera.start_preview()
    
        camera.start_recording('/home/pi/Desktop/video.h264')
    
        time.sleep(30)
    
        camera.stop_recording()
    
        camera.stop_preview()

You'll notice I've set the _time.sleep()_ value to 30, meaning the script will start recording, wait for 30 seconds, then stop. Save this script as **videocapture.py**, and press F5 to run.

Notice the use of the _camera.start_recording()_ function. This saves the footage as a file called **video.h264**, a high definition video clip that you can open from the Raspbian desktop. The best way to do this is to browse to the Desktop folder (or whatever your chosen file path in the above script is), press F4 to open the terminal and enter
    
    
    omxplayer video.h264

Add a suitable battery for the Raspberry Pi and a display, and you've got yourself a compact camcorder!

## Time-Lapse Photography

[Time-lapse photography](http://www.makeuseof.com/tag/4-ways-to-take-time-lapse-videos/) has increased in popularity with the explosion of smartphone cameras in the past few years, making what was once the province of specialist photographers accessible by almost everybody.

The downside of using a smartphone for that sort of photography is obvious; it is time consuming, and hogs a resource that you might need for, well, making and receiving phone calls. The Raspberry Pi with its attached camera makes a good alternative, and with a battery attached can prove just as portable and versatile as an Android or iPhone app, and makes more sense than just using your [Pi as a time-lapse trigger for a DSLR](http://www.makeuseof.com/tag/how-to-capture-time-lapse-photography-with-your-raspberry-pi-and-dslr-or-usb-webcam/).

Before proceeding, install ffmpeg:
    
    
    sudo apt-get install ffmpeg

Then, use this Python script to capture the time lapse images:
    
    
    import time
    
    import picamera
    
     
    
    VIDEO_DAYS = 1
    
    FRAMES_PER_HOUR = 60
    
    FRAMES = FRAMES_PER_HOUR * 24 * VIDEO_DAYS
    
     
    
    def capture_frame(frame):
    
        with picamera.PiCamera() as cam:
    
            time.sleep(2)
    
            cam.capture('/home/pi/Desktop/frame%03d.jpg' % frame)
    
     
    
    # Capture the images
    
    for frame in range(FRAMES):
    
        # Note the time before the capture
    
        start = time.time()
    
        capture_frame(frame)
    
        # Wait for the next capture. Note that we take into
    
        # account the length of time it took to capture the
    
        # image when calculating the delay
    
        time.sleep(
    
            int(60 * 60 / FRAMES_PER_HOUR) - (time.time() - start)
    
    )

![muo-diy-picamera-timelapsesnaps](http://cdn.makeuseof.com/wp-content/uploads/2015/08/muo-diy-picamera-timelapsesnaps.png?x58476)

You've created a collection of images recorded over a 60 minute period with this script. To view the images as a film, compile the images as follows:
    
    
    ffmpeg -y -f image2 -i /home/pi/Desktop/frame%03d.jpg -r 24 -vcodec libx264 -profile high -preset slow /home/pi/Desktop/timelapse.mp4

You can run the video in your Raspberry Pi with a Terminal command:
    
    
    omxplayer timelapse.mp4

The video will then be played full screen. It might look something like this…

## The Raspberry Pi Security Camera

We've previously explored how to build a home webcam [security system with your Raspberry Pi](http://www.makeuseof.com/tag/build-a-motion-capture-security-system-using-a-raspberry-pi/), with a tutorial that predated widespread availability of the Pi's dedicated camera. Things have of course changed since then, but you can use the same principles and software to turn the Pi into a far more compact security camera solution. In theory, you can monitor the comings and goings in and out of your house for under $100 using one or more Raspberry Pi security cameras.

We've given you five uses for your Raspberry Pi camera module, but we reckon you might be able to add to the list. **How do you use yours? Tell us in the comments.**
