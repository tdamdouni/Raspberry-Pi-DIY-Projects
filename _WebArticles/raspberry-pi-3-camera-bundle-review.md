# Raspberry Pi 3 Camera Bundle - Review

_Captured: 2017-11-23 at 21:38 from [www.element14.com](https://www.element14.com/community/roadTestReviews/2544/l/Raspberry-Pi-3-Camera-Bundle?CMP=SOM-TWITTER-PRG-ROADTEST-REVIEW-RASPI-PI3CAMERABUNDLE-COMM-GBL)_

**Product Performed to Expectations:**
10

**Specifications were sufficient to design with:**
10

**Demo Software was of good quality:**
10

**Product was easy to use:**
10

**Support materials were available:**
10

**The price to performance ratio was good:**
10

**TotalScore:**
60 / 60 

  * **Evaluation Type:** Development Boards & Tools 
  * **Was everything in the box required?:** Yes 
  * **What were the biggest problems encountered?:** Using an existing Raspbian installation to build an auto-booting camera system can be a bit fickle - consider a purpose-build OS like motionEYE if you want something easier to configure. 
  *   

  * **Detailed Review:**

Received the Pi Camera and Pi 3 from element14 and started taking a look! 

![](https://lh5.googleusercontent.com/ZoUrgSvneyz1sqkwFpNlUk--d6k_qANiTDxgVrMQMBWGemN2GFK4k90YdP0M8ao7qSg1AYcfwKLSUzrIAcYRAkhgTI3PvejMqYkQs-oYLs6tEF041SPzKv0DVLwJmIuw2PkzCPY)

![](https://lh5.googleusercontent.com/y96qfGvzHwxqTrV82t-tpT4Z_YzodmV0x5hRuHEHUTjVTd4cjQ2XRCaXc8m3SldZhQK-rqHqBiAS_G2-wvJjzlEwbePEfH6iMLhGz_jk4rbkCWdETYudoLUaGgjQHjnGcuQhhrU)

**Raspberry Pi**

Raspberry Pi is a lovely little unit with several capabilities. With a CPU, RAM, and many peripheral connections, this little beauty can be a full fledged computer. Many people are building their own small computers and terminals with these units.

I've done a couple basic projects with it to set up home media centers and demonstrate internet connectivity, and also tested the senseHAT's light display and sensing functionalities in an interactive motion demo that allows children (or adults!) to rotate a 3D model of a spaceship, using readings from the senseHAT's accelerometer and gyroscope.

Camera

This great little camera connects to any of the Pi series via ribbon cable. The Pi Camera comes on a little breakout board with holes on the 4 corners, to allow for easy mounting of the breakout into a case assembly. A nice design choice is that the ribbon cable is removable from the breakout board (not just the Pi side), allowing you to swap the ribbon cable out if you need a newer replacement or a different length. The camera module itself is also removable from the breakout board, adding further modularity and replacement options.

![](https://lh5.googleusercontent.com/OR0MnKhvyYsKqR3ubgnXPrVwGwGD7F3x45Fr9JhFMMjZtjn8mvnjK8aK4-aYYT5Pb5u-0NU4GwGm5Pe8HFjmk8i2L6zFE4k6M9WYdZYhwhm3FqRAiPBh1S75_rIVU1ea_-1UVj8)

> _Installation_

Everything looks great out of the box and connects fairly easily. The ribbon cable connects fairly easily, and then you lock down the connector. The stock ribbon cable is fairly long. I suggest finding a shorter cable or 3D printing a camera housing asap to protect the unit and its lens. Or try to get handy with some materials to protect the little unit 

![](https://lh5.googleusercontent.com/kHY1hifSrAmebbR5Aucxa2b3acDPrhmHlt9lrY49skykgXQkouX4LvzfJJR7GV6GQ-QFJnjVKmHo3a2fwdJO2aOs2eYlhXe5NvO5HnXFqXmmhobcBlZVB_COebdw4jLtbiy9ReI)

I had a Raspbian install already deployed to a micro SD card so I commenced with this existing system. Boot into the system, and run a few things to get started. Update your system (sudo apt-get update, and then sudo apt-get upgrade), and ensure that camera support is enabled (Open terminal and type sudo raspi-config to check)

Basic photo 

There are several great guides to getting rolling quickly with the camera. You can take photos in the native Pi Terminal:

Following command will take a picture and save it as a .jpg file

![](https://lh4.googleusercontent.com/1QCVUpkhhi25B7YeX0KO0DGWDFvbzsOmQo782F-sucGrA1D3yCtNwwb963Rzdispscnoc5R35pYH80BST3DYHVsE7NDnc_BmNSuRuMU900NS0uOxcFVUTBrjNiTpndRoFwS5wuA)

Also easy: Record a video. Note that you add flags here to specify the recording length, in ms.

Alternatively, you can use Python and the PiCamera library for more full-featured control, and the ability to easily create python scripts to save images. Open a terminal and type "python" to begin. The beauty of this camera is the great library support available to customize your pictures. Check here for a great guide on basic picture taking: [https://projects.raspberrypi.org/en/projects/getting-started-with-picamera](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fprojects.raspberrypi.org%2Fen%2Fprojects%2Fgetting-started-with-picamera) . Gives some great steps on adding photo effects, flipping the image, changing resolution, etc. Some great example code exists, such as showing you how to take fast burst photos or time lapse photography.

Security Camera Project

I tried following Adrian Rosebrock's guides on installing OpenCV for Raspberry Pi but I frequently run into issues. This latest attempt had errors likely because I initially followed his guides for Raspbian aspian Jessie, but I had installed Raspbian Stretch. In any case, I got frustrated enough to consider the standard install command using pre-complied binaries, and this has worked to run all subsequent scripts in my demo. This is also much faster than Adrian's guide, which can take one hour to compile.

Open a terminal and do the following to confirm an install

You should get a confirmation!

Using OpenCV and Adrian's guides, you can fairly quickly build a great home security system using the Pi and its camera. I followed Adrian's guide and changed steps along the way: [https://www.pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fwww.pyimagesearch.com%2F2015%2F06%2F01%2Fhome-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv%2F)

In this guide you setup a script that continuously acquires raw frames from the Pi. The latest frame is compared to prior frames to establish instances of movement in an otherwise still scene. If movement is detected, the specific areas of movement can be localized, and a bounding box is drawn around the area of the intruder. Notice in my workspace image below: The local areas of movement are isolated and highlighted.

![](https://lh4.googleusercontent.com/vkArddoUuSZmHllTt1llil6IU2kRVQQKg3ahViy6966zz4nz8tUo5LSZ7s8Rq4DUPvGaJQuCIvOSobaZdvkuGz85rcNhdADq01iEC-ZyDjpgFXzMRG65VY06xhZ6KB2HddG5HXU)

Adrian's script used a Dropbox API to easily upload the images to personal Dropbox servers, but I opted to upload images to Google Drive servers instead. I found a couple resources to get me rolling with the Drive API and make it more Pi friendly. The standard Google resources ([https://developers.google.com/drive/v3/web/quickstart/python](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fdevelopers.google.com%2Fdrive%2Fv3%2Fweb%2Fquickstart%2Fpython)) help you set up your API access and public/private tokens, and this StackOverflow page gives a great overview ([https://stackoverflow.com/questions/24419188/automating-pydrive-verification-process](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F24419188%2Fautomating-pydrive-verification-process)) on how to load credentials from a file, so that the system runs autonomously after the first browser auth. Some future authentications may be needed if the token expires! Note that I also used the Python library PyDrive to make Drive access more user friendly ([https://pypi.python.org/pypi/PyDrive](https://www.element14.com/community/external-link.jspa?url=https%3A%2F%2Fpypi.python.org%2Fpypi%2FPyDrive)). This allows you to read, write, and upload files in a very user-friendly manner.

![](https://lh6.googleusercontent.com/7-4B4wowMg0zVmTBVjSHe_XaVn3ZSTqYQiFKfLst1auikVFBpEDLsTae0n1q1YrhyyC4EK9oWGHY7CfY7X3xoqiF5ZxHo8rVxJbxc0NU1pfXTz067oCaJXScfZjR91CIt2bpxGQ)

The system is quite fast: I see the notification on the Pi and the file appears in Drive just seconds later. Definitely responsive enough for integration into some serious security system.

![](https://lh5.googleusercontent.com/RnGICTqYG45PmL-PEX2HG_cRoek-GqPpHRX7wTtWAA3RIBWbzlxDUDbWEHCJssipk4BaHocOptg0uYhJizwbRRSOHBQTXSR-DQfhJScIM6D0u3vi2yAdDr0C3Fsm9xqTFpLNYCk)

Here are a couple shots from the system in action

![](https://lh4.googleusercontent.com/VhGSHSlV1scPWlUDNYc9WcXAU8ctd_m_3NIlhbgeW1zr7506yEuMZTLZGMJZFHX0nmJeHO_-xJhMpJbeZVJgTpTK20BTc7BwJ5YrRhCiQb6GUFG04rXJ_vl9fcD7WQb0xPFCPjc)

![](https://lh4.googleusercontent.com/1_Qaa0NvnCV-DGpar5qJ6w1dxNne-PpB73AsnNnHF9DfScXm__ihHwe8Wo5FeA52uyTWrFXN_mJj2NdRb6vT_XvKUG10emq4gtHUfN5ThhgMVMO-91x-SxcEGrr7tmyNAT_s71A)

**Executing on startup in Raspbian**

One issue I have been running into with Pi is trying to get this python script to automatically execute on startup, so that I can more easily run this application in a headless or auto-booting scenario.

I added a line to ~/.config/lxsession/LXDE-pi/autostart to execute a python script in the past, but had issues doing similar with my Python script this time around

**Conclusion**

This Pi Camera is a great little unit with decent image quality and lighting performance. It's definitely a great way to add more possibilities home hobby projects for kids, or to build a DIY security system on a budget.

Code from my project can be found below. Note that you need to configure your own Dropbox or Drive API if you want file uploading to work. Also you need to build your own version of the conf.json file to configure the python script execution.

For more context on the Pi Camera rating, I give the hardware and software high ratings because of the good price, size and easy connection of the hardware, and the great online resources for native control of the camera as well as a great Python library for image capture and image processing. Only improvement I can think of: Offer some camera housing with the product. At the minimum offer some sort of two piece enclosure or stand which the user can then fix to stationary objects.

As a python and photography geek, I have many other projects I want to try out. But with crunch time at school approaching, I figured I should submit this quick review before things get hectic!
