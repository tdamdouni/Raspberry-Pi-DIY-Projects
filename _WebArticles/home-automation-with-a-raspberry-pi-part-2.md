# Home Automation With a Raspberry Pi (Part 2)

_Captured: 2017-05-19 at 11:17 from [dzone.com](https://dzone.com/articles/home-automation-with-a-raspberry-pi-part-2?edition=298101&utm_source=Daily%20Digest&utm_medium=email&utm_campaign=dd%202017-05-15)_

In our most [recent blog](https://dzone.com/articles/home-automation-with-a-raspberry-pi-part-1), we talked about software installation to set up and begin automating home appliances using human hand gestures to control them.

We are now in the second part of this series, where we intend to develop an application that is built on a [Raspberry Pi](https://www.raspberrypi.org/) using [Java](http://www.azilen.com/technology/enterprise-web/java/) and computer vision APIs. It will detect hand gestures and consequently pass the signals to an IR device, which will then perform the appropriate home automation.

This blog guides you through the complete procedure for detecting human hand gestures and interacting with hardware/home appliances.

Let us first have a look at the role of the application in implementing hand gesture recognition for home automation.

Here is our process:

  * The application and IR device must be part of the same network.
  * The application captures camera input continuously.
  * From captured image frames, the hand gesture is detected using OpenCV data structures/algorithms.
  * Appropriate signals are found and consequently passed onto the IR device (HTTP call) with the proper command (ON/OFF) to the external device.

## **Core Functionalities and Modules**

  * **Gesture detection:** The application contains open computer vision APIs. OpenCV and JavaCV process the camera input and apply algorithms to process their frames.
  * **SmartConfig: **This is the heart of the application, which can talk with the IR device to control an external device. This module has two modes: Learning and Execution. In Learning mode, it configures the IR device using the TI Smart config protocol. It monitors and records data sequences for different infrared sequences for home appliance operations. During Execution mode, it can send the recorded sequences to the IR device, which are converted by the IR device into an infrared sequence to control different devices.
  * **Signal processing: **This is the remote processing part of the application, in which the application stores the signals and passes them to the IR device for further operations.

Let's have a look at the technologies used in implementing hand gesture recognition.

## **OpenCV**

In our project, we use OpenCV contours for recognizing the hand image.

Contours can be explained simply as a curve joining all the continuous points (along the boundary), having the same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition. For better accuracy, use binary images. So before finding contours, apply a threshold or canny edge detection. The findContours function modifies the source image. So if you want the source image even after finding contours, store it to some other variables.

In OpenCV, finding contours is like finding a white object from a black background. So remember, an object to be found should be white and the background should be black.

### **Method/Algorithms to Detect Hands From Video**

Briefly, let's look at the several ways to process a frame to detect the hand and their gestures:

  * **Background subtraction**: A simple method to start with is subtracting the pixel values. However, this will result in negative values and values greater than 255, which is the maximum value used to store an integer. And what if we have a black background? Nothing gets subtracted in that case. Instead, we use an inbuilt background subtractor based on a Gaussian Mixture-based background/foreground segmentation algorithm. Background subtraction involves calculating a reference image, subtracting each new frame from this image and the threshold. The result is a binary segmentation of the image, which highlights regions of non-stationary objects. We then use erosion and dilation to enhance the changes to make it more prominent.
![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/background_subtraction.jpg)

  * **Color detection**: Skin color detection is one of the most popular methods. This method is simple and depends on skin color, which can be white, black, or other colors. It also considers environment light conditions as well as the background.

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/color_detection.jpg)

  * **Edge detection**: An edge detection operator uses a multi-stage algorithm to detect a wide range of edges in images. Its aim is to satisfy these criteria:  

    * Lower error rate
    * Good localization
    * Minimal response
![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/edge_detection.jpg)

For our solution, we used the color detection method to detect hands from the frame via user skin color. The application itself has a GUI to detect user hand skin color and to persist it for further application uses.

After analyzing the application side requirements, let's move on to midway device for further communication, referred to here as our **IR device.**

## **IR Device**

The IR device works as an IR transceiver. It is used to record IR commands for different appliances, and that recorded sequence is used to control appliances based on different gestures detected in the previous phase. The IR device can be connected to a TV, set-top boxes, stereos, air conditioners, and other appliances, and then can pass an infrared remote control signal and start the home appliance.

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/IR-device.jpg)

After understanding the all the devices, let's now understand the procedure to develop the application.

## **Guide to Develop the Application**

Home automation is the residential extension of building automation and involves the control and automation of lighting, air conditioning, and security, as well as home appliances such as washers/dryers, television, ovens, or refrigerators/freezers using Wi-Fi for remote monitoring.

Modern systems generally consist of switches and sensors connected to a central hub, sometimes called a "gateway," from which the system is controlled with a user interface that is interacted either with a wall-mounted terminal, mobile phone software, tablet computer, or a web interface, often, but not always, via Internet cloud services.

The application we have developed has a user interface that is able to manage devices and communication paths. It has a robust feature to make devices habituate via their Learning Mode and Execution Mode.

## **SmartConfig**

It's a Wi-Fi setup process that allows multiple in-home devices to connect to Wi-Fi networks quickly and efficiently. It is specifically for applications that typically do not have a display or keyboard to enter network name and password.

The SmartConfig interface gives end users the ability to easily connect IR devices to an access point. Through a simple SmartConfig method/interface, consumers can use any programming concept to create their own application using the SmartConfig Interface.

To connect the IR device/hardware with the application, send broadcast datagram packets with network (Wi-Fi) details (SSID and Password).

This process is able to send and receive broadcast datagram packets and make a connection with the application and IR hardware device. The application has a GUI that allow the user to connect to the device.

The application first checks whether any IR device is already connected. If not, then it will prompt a window to connect the device with some validations:

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/ssid.jpg)

The application creates a socket connection with the host (router) and sends broadcast datagram packets with the SSID and password to connect with the IR device and waits for an acknowledgment from the IR smart device.

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/1.jpg)

**Device learning**: After the IR device is connected to the application, the user is able to set up commands/signals for home appliances based on their hand gestures, and it starts with a learning step.

In the learning phase, a user is able to set up one or multiple instructions or commands for multiple devices using the GUI of application.

Our current implementation has basic gestures like a 0-5 count, up-down, and left-right. Based on user configuration, the application will operate their attached devices.

For example, let's increase our TV volume with an up and down motion of the hand.

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/device-setup.jpg)

After the learning phase, you are ready to operate your home appliances with your hand gestures. Now, users can turn a TV on and off and also manage its volume in our application implementation.

We have configured six or seven commands to operate TV, like on, off, volume up-down, mute, open menu bar, exit menu bar, and their operations.

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/2.jpg)

**Signal processing (remote service)**: Our application is able to detect hand gestures and pass the IR signal to configured home appliances depending on human hand gestures.

The application is capable of managing user interactions, IR device communication, signals, and skin color persistence.

The application gateway is incorporated to connect smart home appliances, and an IoT connection management platform is required to enable various applications.

These applicable solutions include: home automation, which, ideally, promotes a happier, more comfortable, and convenient lifestyle.

The solution will help operators transform from traditional home broadband services to provide intelligent home services.

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/3.jpg)

> _IR Signal Execution (IR signal transmission)_

![Image title](http://www.azilen.com/blog/wp-content/uploads/2017/02/4.jpg)

## **Conclusion**

Home automation is a significant undertaking in the IoT domain. With improved convenience, comfort, energy efficiency, and security under the IoT domain, it has proved to be incredibly beneficial for both individuals and society.

In our next blog, we are going to look at the real-time working application demo and step-by-step code snippets of the application. So let's grab the opportunity and see what the next blog brings.
