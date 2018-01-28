# Facial Recognition Lost Child Finder

_Captured: 2017-12-06 at 12:49 from [www.hackster.io](https://www.hackster.io/PaulTR/facial-recognition-lost-child-finder-7675f9?ref=challenge&ref_id=104&offset=9)_

![Facial Recognition Lost Child Finder](https://hackster.imgix.net/uploads/attachments/358874/img_20170915_145155_P1xp71fFvK.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

One of the scariest things that can happen to a parent is losing a child in a crowded place. However, while I worked at a zoo, this was a surprisingly common occurrence, as children tend to wander off like curious ninjas. When this happened, standard procedure was that a parent would notify any staff, and they'd call it over the walkie-talkies with a description and name of the child while other staff watched each exit of the zoo.

While this problem was usually resolved relatively quickly by staff spotting the child, I thought it would be interesting to figure out how to create a simple and affordable solution where an image could be uploaded somewhere and a link could be sent to a device that would then take pictures and attempt to recognize the child through facial recognition. Once the child is found, the device could then notify staff of the general location.

There are two major parts to this project: communication and facial recognition. One problem that we ran into at the zoo is that WiFi isn't available in most locations, however cellular connections were pretty good since the zoo was located in the middle of a large public park in the city.

![](https://hackster.imgix.net/uploads/attachments/383998/screen_shot_2017-11-23_at_9_51_19_pm_DCJMGUPOsQ.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Because of the network limitations of the location, Hologram and their connectivity platform seemed like a worthwhile solution for the first portion of this project. There is one part where I ran into a problem - downloading the image needed for face recognition. Because of this, I can only use Hologram on the person-to-device boundary, though I will hopefully be able to update the demo as more capabilities are added to the SDK.

Facial recognition is where things get a bit more tricky. Luckily, there is a great [open sourced library](https://github.com/ageitgey/face_recognition) for facial recognition that works on the Raspberry Pi by a developer named Adam Geitgey. If you're interested in how this library works, I strongly recommend reading his article [here,](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78) otherwise the **tl;dr** is that a known face in an image is turned to gray scale, the image is subdivided into sections and the direction of light in the image is measured and stored, then when a new image is taken, any detected faces in that new image are similarly encoded and compared to the original known image.

![](https://hackster.imgix.net/uploads/attachments/384001/encoding_475fhhZJR7.png?auto=compress%2Cformat&w=680&h=510&fit=max)

> _Encoding for an image of Will Farrel_

Now that we know the two tools that we're going to use for our project, it's time to setup a device that can support both. This project will use a Raspberry Pi Zero W with a Raspberry Pi camera module running a Python 2.7 script with a Hologram Nova. You can start by [installing Raspbian](https://www.raspberrypi.org/downloads/raspbian/) on your Pi Zero W. I also strongly recommend using a USB shield with the Pi Zero so that you can connect a mouse and keyboard to it alongside a Hologram Nova. This is how my setup looked during development once I got fed up with swapping the keyboard and mouse USB.

![](https://hackster.imgix.net/uploads/attachments/384262/img_20171123_155419_1vTSXoOX1T.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Before you can dive into working with face recognition on the device, you'll need to install a lot of dependencies. Since the Pi Zero W is slow, this actually took me about 3 days of just starting the installs, letting them run, and then checking in on them later to start the next install. You can find the instructions for setting up dlib and the face recognition library in this [gist](https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65). You'll also need to install git before setting up the library and a variety of python dependencies for running face recognition ([scipy](https://www.scipy.org/), [pi-camera](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera), [numpy](http://www.numpy.org/), a few others). It's worth noting that those instructions are for Python 3, but the Hologram SDK requires Python 2.7. You can use `pip2` and `python` commands instead of `pip3` and `python3` to use the older version of dependencies and the face recognition library. Because of the limited memory on the Pi Zero W, you'll probably also run into a memory issue while installing the face recognition library. You can get around this with the command `pip2 --no-cache-dir install face_recognition` .

Once you're done with dependencies and configuration for the face recognition library, you should be able to run the following script to test it.
    
    
    import face_recognition
    import picamera
    import numpy as np
    camera = picamera.PiCamera()
    camera.resolution = (320, 240)
    output = np.empty((240, 320, 3), dtype=np.uint8)
    print("Loading known face image(s)")
    face_img = face_recognition.load_image_file("face_img.jpg")
    trained_face_encoding = face_recognition.face_encodings(face_img)[0]
    face_locations = []
    face_encodings = []
    while True:
       print("Capturing image.")
       camera.capture(output, format="rgb")
       face_locations = face_recognition.face_locations(output)
       print("Found {} faces in image.".format(len(face_locations)))
       face_encodings = face_recognition.face_encodings(output, face_locations)
       for face_encoding in face_encodings:
           match = face_recognition.compare_faces([trained_face_encoding], face_encoding)
           name = "<Unknown Person>"
           if match[0]:
               name = "Paul"
           print("I see someone named {}!".format(name))
    

You can find an example (albeit slightly modified to print the encoding of unrecognized faces for testing purposes) of the above script working here.

Once face recognition is working, it's time to add Hologram support to your script. First, install the Hologram Python SDK with the following command: `curl -L hologram.io/python-install | bash`

Once the SDK is installed, you can start writing a Python script that will do the following:

  * Receive a URL for an image via SMS
  * Download that image into the script's directory
  * Encode the face in the image and store it locally
  * Take pictures and check for faces
  * If a face is detected, compare it to the stored encoding to determine if the child was found
  * Notify a set number about the detection

(_full disclosure, I typically do Android development, so am learning Python syntax as I go along. I'm sure this script can be improved. Right now it's just in a "make it work" phase_)

To do the above, you will need to include these imports at the top of the script
    
    
    import face_recognition 
    import picamera 
    import numpy as np 
    from Hologram.HologramCloud import HologramCloud 
    import urllib 
    

The first three are for face recognition, the fourth is for accessing the Hologram SDK, and the final is a library for downloading images from a URL.

Next, initialize the Raspberry Pi camera and two arrays that will be used for working with face locations and encodings from images taken by the camera. This demo is using a standard Raspberry Pi camera module set to a low resolution, but could use a better camera later.
    
    
    camera = picamera.PiCamera() 
    #For a non-demo, use a better camera with higher resolution 
    camera.resolution = (320, 240)
    camera_name = "demo" 
    output = np.empty((240, 320, 3), dtype=np.uint8)
    face_locations = [] 
    face_encodings = [] 
    

You will also need to initialize some values for the Hologram Nova. This block of code will initialize HologramCloud with `csrpsk` authentication (which is required for SMS messages), enable SMS messaging, create a dictionary with the Nova's device key, and create a value for the phone number that will be notified when a face is recognized.
    
    
    credentials = {'devicekey': '8-character-key-from-dashboard'} 
    cloud = HologramCloud(credentials, network='cellular', authentication_type='csrpsk') 
    cloud.enableSMS() 
    phone_number = "+15551234567" 
    

You can find the device key for your Hologram Nova after creating an account on Hologram.io, registering and activating your Hologram SIM chip, and going into the dashboard to generate a device key.

![](https://hackster.imgix.net/uploads/attachments/384199/screen_shot_2017-11-24_at_10_23_08_am_Dl91tl2oGU.png?auto=compress%2Cformat&w=680&h=510&fit=max)

While you are in the dashboard, you will also need to create a phone number and assign it to the Hologram Nova. This should cost about $1. After that is done, you should see the phone number under the device's configuration screen.

![](https://hackster.imgix.net/uploads/attachments/384205/screen_shot_2017-11-24_at_10_31_11_am_cgcU5N0Ezi.png?auto=compress%2Cformat&w=680&h=510&fit=max)

After you have finished with the setup steps for your script, you can create a constantly running loop that will listen for a received text with a URL of a face to recognize.
    
    
    while True: 
       sms_obj = cloud.popReceivedSMS() 
       if sms_obj is not None:  
    

If there's no SMS messages on the stack, then the `sms_obj` will be `None` . Once a text is received, `sms_obj` will be initialized and we can use extract information from it. In this case, we will simply download an image from a URL sent in the message body. Once we have the image downloaded and saved, we can encode it and store that data.
    
    
    print sms_obj.message 
    urllib.urlretrieve(sms_obj.message, "lost_child.jpg")
    child_image = face_recognition.load_image_file("lost_child.jpg") 
    child_encoding = face_recognition.face_encoding(child_image)[0] 
    

Once an image has been received and encoded, the device should loop through taking images and checking them for the lost child. This can be done by capturing an image with the Pi's camera and locating faces in that image. If faces are detected, they are then encoded and checked for a match against our original image.
    
    
    camera.capture(output, format="rgb") 
    face_locations = face_recognition.face_locations(output) 
        if len(face_locations) > 0: 
            print("Found {} faces in image.".format(len(face_locations))) 
            for face_encoding in face_encodings: 
                match = face_recognition.compare_faces([child_encoding], face_encoding) 
    

If a match is detected, the device will send an SMS to the number we defined earlier in the script with information about the device's location so that someone can go to that area.
    
    
        if match[0]: 
            recv = cloud.sendSMS(phone_number, 'Child found at camera: ' + camera_name) 
            print 'response message ' + cloud.getResultString(recv) 
    

The text may be any string content. The above snippet should produce the following text message

![](https://hackster.imgix.net/uploads/attachments/384618/screenshot_20171125-054330_jHflzTc502.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Once the script is written and running on the Pi Zero W (either manually started or adjusted to start automatically on device bootup), users will need to obtain a picture of the person that is being searched for and upload it somewhere where they can receive a link to the image. For testing this, I uploaded an image to Firebase Storage and obtained a URL from the data for that file.

![](https://hackster.imgix.net/uploads/attachments/384249/screen_shot_2017-11-24_at_10_56_52_am_xqGm3HUHhC.png?auto=compress%2Cformat&w=680&h=510&fit=max)

Because SMS has a limit of 160 characters, I also ran this URL through bit.ly to shorten it to a reasonable size.

![](https://hackster.imgix.net/uploads/attachments/384248/screen_shot_2017-11-24_at_10_57_04_am_CvNmvvENBQ.png?auto=compress%2Cformat&w=680&h=510&fit=max)

From the Hologram dashboard for your Nova, you can post the URL in the **via SMS** tab of **Messaging** to send it to your Pi.

![](https://hackster.imgix.net/uploads/attachments/384252/screen_shot_2017-11-24_at_10_59_36_am_2TfN38p0I9.png?auto=compress%2Cformat&w=680&h=510&fit=max)

This will kick off the process of downloading the image and looking for the lost child.

Now that you have the base process down, you can play around with extending the functionality to a faster device or using this as a component of other projects that could use local face recognition or the Hologram SDK. Good luck, and have fun!

  * Download the image via a cell network (doesn't seem to be possible with the current Hologram SDK)
  * Better camera
  * More efficient Raspberry Pi with fan to prevent overheating
  * Write a backend program that allows users to text an image that will be uploaded and automatically update the Pi devices. 
