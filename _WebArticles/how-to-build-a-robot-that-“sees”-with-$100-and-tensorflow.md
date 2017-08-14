# How to build a robot that “sees” with $100 and TensorFlow

_Captured: 2017-08-05 at 17:16 from [www.oreilly.com](https://www.oreilly.com/learning/how-to-build-a-robot-that-sees-with-100-and-tensorflow)_

![Eye of Providence.](https://d3tdunqjn7n0wj.cloudfront.net/1440x960/all_seeing_eye_crop-d6da5ba2ed73e411825c69095136f431.jpg)

> _Eye of Providence._

Object recognition is one of the most exciting areas in machine learning right now. Computers have been able to recognize objects like faces or cats reliably for quite a while, but recognizing arbitrary objects within a larger image has been the Holy Grail of artificial intelligence. Maybe the real surprise is that human brains recognize objects so well. We effortlessly convert photons bouncing off objects at slightly different frequencies into a spectacularly rich set of information about the world around us. Machine learning still struggles with these simple tasks, but in the past few years, it's gotten much better.

Deep learning and a large public training data set called [ImageNet](http://www.image-net.org/) has made an impressive amount of progress toward object recognition. [TensorFlow](https://www.tensorflow.org/) is a well-known framework that makes it very easy to implement deep learning algorithms on a variety of architectures. TensorFlow is especially good at taking advantage of GPUs, which in turn are also very good at running deep learning algorithms.

## Building my robot

I wanted to build a robot that could recognize objects. Years of experience building computer programs and doing test-driven development have turned me into a menace working on physical projects. In the real world, testing your buggy device can burn down your house, or at least fry your motor and force you to wait a couple of days for replacement parts to arrive.

![Architecture of the object-recognizing robot](https://d3ansictanv2wj.cloudfront.net/Figure_1-1ad2b142be6ca8641212c7579ab4f95d.jpg)

> _Figure 1. Architecture of the object-recognizing robot. Image courtesy of Lukas Biewald._

The new third generation [Raspberry Pi](https://www.amazon.com/Raspberry-Pi-RASP-PI-3-Model-Motherboard/dp/B01CD5VC92) is perfect for this kind of project. It costs $36 on Amazon.com and has WiFi, a quad core CPU, and a gigabyte of RAM. A $6 [microSD card ](https://www.amazon.com/Silicon-Power-MicroSDHC-Class10-SP016GBSTHBU1V20SP/dp/B00TDBLTWK/ref=sr_1_3?s=pc&ie=UTF8&qid=1473285120&sr=1-3&keywords=micro+sd+card+16)can load [Raspberian](https://en.wikipedia.org/wiki/Raspbian), which is basically [Debian](https://en.wikipedia.org/wiki/Debian). See Figure 1 for an overview of how all the components worked together, and see Figure 2 for a photo of the Pi.

![Raspberry Pi](https://d3ansictanv2wj.cloudfront.net/Figure_2-985cd20ea0c0bcd68a7d896f11312edf.jpg)

> _Figure 2. Raspberry Pi running in my garage. Image courtesy of Lukas Biewald._

I love the [cheap robot chassis](https://www.amazon.com/SainSmart-Smart-Chassis-Tracing-Encoder/dp/B00NDXEUM0/ref=sr_1_cc_1?s=aps&ie=UTF8&qid=1473285343&sr=1-1-catcorr&keywords=sainsmart+chassis) that Sain Smart makes for around $11. The chassis turns by spinning the wheels at different speeds, which works surprisingly well (see Figure 3).

![Robot chassis](https://d3ansictanv2wj.cloudfront.net/Figure_3-aab0fcf7f65ef4ec2935813e254c68f8.jpg)

> _Figure 3. Robot chassis. Image courtesy of Lukas Biewald._

The one place I spent more money when cheaper options were available is the [Adafruit motor hat](https://www.adafruit.com/products/2348?gclid=Cj0KEQjw9b6-BRCq7YP34tvW_uUBEiQAkK3svWdaQW4i4uk0D0W2D0yQulnfo8Z09ul57dAEQsMJe2gaAu9e8P8HAQ) (see Figure 4). The DC motors run at a higher current than the Raspberry Pi can provide, so a separate controller is necessary, and the Adafruit motor hat is super convenient. Using the motor hat required a tiny bit of soldering, but the hardware is extremely forgiving, and Adafruit provides a nice library and tutorial to control the motors over [i2C](https://en.wikipedia.org/wiki/I%C2%B2C). Initially, I used cheaper motor controllers, but I accidentally fried my Pi, so I decided to order a better quality replacement.

![Raspberry Pi with motor hat and camera](https://d3ansictanv2wj.cloudfront.net/Figure_4-ed9055c22840d6a0fa9088bf4fa52ea7.jpg)

> _Figure 4. Raspberry Pi with motor hat and camera. Image courtesy of Lukas Biewald._

A [$15 camera](https://www.amazon.com/Arducam-Megapixels-Sensor-OV5647-Raspberry/dp/B012V1HEP4/ref=sr_1_2?s=electronics&ie=UTF8&qid=1473286363&sr=1-2&keywords=raspberry+pi+camera) attaches right into the Raspberry Pi and provides a real-time video feed I can use to recognize objects. There are tons of awesome cameras available. I like the infrared cameras that offer night vision.

The Raspberry Pi needs about 2 amps of current, but 3 amps is safer with the speaker we're going to plug into it. iPhone battery chargers work awesomely for this task. Small chargers don't actually output enough amps and can cause problems, but the [Lumsing power bank](https://www.amazon.com/gp/product/B01DU4E7EW/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1) works great and costs $18.

A couple of [HC-](https://www.amazon.com/CJRSLRB%C2%AE-Ultrasonic-Measuring-Transducer-Duemilanove/dp/B016XJABP0/ref=sr_1_3?s=automotive&ie=UTF8&qid=1473286270&sr=1-3&keywords=hc+sr04)[SR0](https://www.amazon.com/CJRSLRB%C2%AE-Ultrasonic-Measuring-Transducer-Duemilanove/dp/B016XJABP0/ref=sr_1_3?s=automotive&ie=UTF8&qid=1473286270&sr=1-3&keywords=hc+sr04)[4 sonar sensors](https://www.amazon.com/CJRSLRB%C2%AE-Ultrasonic-Measuring-Transducer-Duemilanove/dp/B016XJABP0/ref=sr_1_3?s=automotive&ie=UTF8&qid=1473286270&sr=1-3&keywords=hc+sr04) help the robot avoid crashing into things--you can buy five for $11.

I added the cheapest USB speakers I could find, and used a bunch of zip ties, hot glue, and foam board to keep everything together. As an added bonus, I cut up some of the packaging materials the electronics came with and drew on them to give the robots some personality. I should note here that I actually built _two_ robots (see Figure 5) because I was experimenting with different chassis, cameras, sonar placement, software, and so forth, and ended up buying enough parts for two versions.

![My 4WD robot and her 2WD older brother](https://d3ansictanv2wj.cloudfront.net/Figure_5-5b104cf7a53a9c1ee95110b78fb14256.jpg)

> _Figure 5. My 4WD robot (right) and his 2WD older sister. Image courtesy of Lukas Biewald._

Once the robot is assembled, it's time to make it smart. There are a million [tutorials](http://www.imore.com/how-get-started-using-raspberry-pi) for getting started with a Raspberry Pi online. If you've used Linux, everything should be very familiar.

For streaming the camera, the [RPi Cam Web interface](http://elinux.org/RPi-Cam-Web-Interface) works great. It's super configurable and by default puts the latest image from the camera in a RAM disk at `/dev/shm/mjpeg/cam.jpg`.

If you want to stream the camera data to a webpage (very useful for debugging), you can install [Nginx](https://en.wikipedia.org/wiki/Nginx), an extremely fast open source webserver/proxy. I configured Nginx to pass requests for the camera image directly to the file location and everything else to my webserver.
    
    
    http {
       server {
          location / {
                proxy_pass http://unix:/home/pi/drive.sock;
             }
                location /cam.jpg {
                    root /dev/shm/mjpeg;
             }
       }
    }
    

I then built a simple Python webserver to spin the wheels of the robot based on keyboard commands that made for a nifty remote control car.

As a side note, it's fun to play with the sonar and the driving system to build a car that can maneuver around obstacles.

## Programming my robot

Finally, it's time to install TensorFlow. There are a couple of ways to do the installation, but TensorFlow actually comes with a makefile that lets you build it right on the system. The [steps](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/makefile#raspberry-pi) take a few hours and have quite a few dependencies, but they worked great for me.

TensorFlow comes with a prebuilt model called "inception" that performs object recognition. You can follow the [tutorial](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/pi_examples) to get it running.

Running `tensorflow/contrib/pi_examples/label_image/gen/bin/label_image` on an image from the camera will output the top five guesses. The model works surprisingly well on a wide range of inputs, but it's clearly missing an accurate "prior," or a sense of what things it's likely to see, and there are quite a lot of objects missing from the training data. For example, it consistently recognizes my laptop, even at funny angles, but if I point it at my basket of loose wires it consistently decides that it's looking at a toaster. If the camera is blocked and it gets a dark or blurry image it usually decides that it's looking at nematodes--clearly an artifact of the data it was trained on.

![Robot plugged in](https://d3ansictanv2wj.cloudfront.net/Figure_6-7737df5765814e0f42aa676c3dfffaf6.jpg)

> _Figure 6. Robot plugged into my keyboard and monitor. Image courtesy of Lukas Biewald._

Finally, I connected the output to the [Flite](http://www.festvox.org/flite/) open source software package that does text to speech, so the robot can tell everyone what it's seeing (see Figure 6).

## Testing my robot

Here are my two homemade robots running deep learning to do object recognition.

## Final thoughts

From 2003 to 2005, I worked in the Stanford Robotics lab, where the robots cost hundreds of thousands of dollars and couldn't perform object recognition nearly as well as my robots. I'm excited to put this software on my drone and never have to look for my keys again.

I'd also like to acknowledge all the people that helped with this fun project. My neighbors, Chris Van Dyke and Shruti Gandhi, helped give the robot a friendly personality. My friend, Ed McCullough, dramatically improved the hardware design and taught me the value of hot glue and foam board. Pete Warden, who works at Google, helped get TensorFlow compiling properly on the Raspberry Pi and provided amazing customer support.
