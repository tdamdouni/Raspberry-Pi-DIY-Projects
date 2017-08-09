# DiY Forest Surveillance Kit

_Captured: 2017-05-19 at 11:40 from [diy.artivis.net](http://diy.artivis.net/)_

_  
Keep an eye on your forest and share it with the world..._

**The design of an open source hardware and software DIY forest surveillance kit is one of the [ARTiVIS](http://artivis.net) project outcomes. The kit aims to repurposes surveillance technology to bring people and their communities together to protect their forests. The kit is common to all the ARTiVIS projects' interactive experiences. Resulting video streams and collected data are expected to be uploaded and then become part of the online platform network for crowdsourced surveillance and artistic manipulation purposes.**  
When available, the kit will also be a seed for community workshops to provide the skills and resources to help deploy new ARTiVIS nodes for artistic experimentation in research centers, festivals, hacklabs and local landmarks.   
**  
KIT DESIGN AND DEVELOPMENT**   
An ARTiVIS kit is composed of a series of hardware modules that can be chosen from common off-the-shelf parts depending on cost, power, network bandwidth or infrastructure restrictions. These hardware modules are controlled by a set of software modules connected to the ARTiVIS online platform

![](http://diy.artivis.net/lib/20120405_diy_v1.png)

In technical terms, the kit is provided as:  
» an open specification for building hardware compatible with the platform  
» an open hardware reference implementation that can be used for community workshops and for the interactive experiences  
» open source software that runs on the kit and interfaces with the platform.

![](http://diy.artivis.net/lib/artivis_diyKit_v1_rasperry5_840.jpg)

> _The image shows the prototype of the ARTiVIS forest surveillance kit with the CPU module based on the Raspberry PI platform, using a USB HD camera as camera module, and a USB mini Wifi adapter as network module._

HARDWARE COMPONENTS

**Power Module** provides power to the whole kit. For the kit's intended function in remote forest locations it is important that it is autonomous in terms of power. This can be accomplished by using a rechargeable power supply, such as a lead or solid state battery coupled with a generating power source like a solar panel, a small wind turbine or a fuel cell.

**CPU Module** is the brain of the system, it connects to all the other hardware modules and runs the ARTiVIS node software. Since the kit's design should take into account both portability and energy efficiency requirements, our first prototypes are being built with the Raspberry Pi, an ARM-based single-board Linux6 computer.

**Camera Module** connects to the CPU Module and provides the images to the CPU for live video streaming. At its simplest configuration, the Camera Module can just be a good USB webcam connected to the CPU Module, but for a more integrated solution we will test interfacing high quality image sensors like the 1080p Leopard image sensor directly to the CPU Module.

**IO Module** interfaces the CPU Module with a set of sensors and actuators that can be read and/or controlled remotely. For this we can use an Arduino board or a similar microcontroller-based IO hardware like the TI Launchpad or rely on the CPU module's native GPIO (General Purpose Input/Output) functionality. For early development this module was skipped since it's not essential for the kit's video streaming functionality.

**Network Module** provides an interface to the Internet for the CPU Module. For early prototyping we used any network connectivity available to the test machine, but for the final reference design we will make use of external USB modems that provide 3G or 4G/LTE connectivity as these are more likely to be available in remote forests than WiFi or wired Ethernet.

SOFTWARE COMPONENTS

The kit's CPU Module runs a set of software applications that allow the kit to perform its task and interface the hardware with the online ARTiVIS server.

**Streaming Service** The streaming service is the heart of the system. At its core it's a video processing pipeline based on the GStreamer framework that captures the live images off the Camera Module, encodes them using a Free lossy codec like Ogg Theora or Webm and streams them to the ARTiVIS server for online distribution. It could also optionally record the video locally for backup purposes.

**IO Service** interfaces with the IO Module hardware, multiplexing access and providing to applications an API that abstracts the underlying hardware, thus permitting access to the sensors and actuators connected to the IO Module.

**Web Service** a web application that runs on an embedded web server on the CPU Module and provides a simple way for the kit's owner to control and configure it. It also provides a REST API that would allow for external control and connectivity to and from the ARTiVIS server to allow uploading of sensor data to the platform and the downloading of actuator commands.

**Server Components** The development of the server software is beyond the scope of the hardware kit's development. For prototyping we are using a streaming server like Icecast and tested the use of open data syndication platforms like GISS (Global Independent Streaming Support) for video and ThingSpeak for sensor data.

**DEVELOPMENT STATUS   
**Early development work on the kit's design was performed throughout the development of the ARTiVIS interactive installations, through field tests of commercial streaming hardware and network connectivity from the forest surveillance tower at Montemor-o-Novo nearby the Play wit Fire residency with mobile Internet access using UStream test, work in first exhibition site, to camera tests at the Laurissilva forest in Madeira.   
The design of initial hardware prototypes was done during the first part of an artist in residency program in Madeira, to connect with the [SINAIS project](http://sinais.m-iti.org/?page_id=2), and are now being further developed for testing during a second residency period in order to become part of the ARTiVIS project's final setup.   
Next we will look into designing the power supply module and testing it for independence and sustainability. Limitations to safeguard and overcome include telecommunications issues related with network signal, strength and speed.

[The ARTiVIS DiY kit Open Source repository](http://gitorious.org/artivis/artivis-diy-kit) includes project schematics and code, hoping to spark a developer community around the project that helps maintain, improve and adapt the kit to specific environments and for other purposes - for instance, replacing expensive hardware setups for remotely watching animal behavior.

![](http://diy.artivis.net/lib/artivis_diyKit_v2_cube.jpg)

> _The image shows the prototype of the ARTiVIS forest surveillance kit with the CPU module based on the CuBox platform, using a USB HD camera as camera module._

Recognizing that "to prevent and control destructive forest fires, the involvement of communities is crucial" [FAO04], we propose to trigger people's participation from the project's grounds, involving the ones willing to contribute to expand the raw material database through a workshop on DIY Forest Surveillance with ARTiVIS.  
The workshop consists of assembling an open hardware kit for forest surveillance and experimentation with real-time video.   
By promoting the ARTiVIS community workshop, we teach participants how to assemble and setup their own ARTiVIS node and explore with them the possibilities offered by real-time video streams of forests.   
We are also planning a developer hackathon to help develop the kit and explore other possible applications.   
If you would like to host an ARTiVIS community workshop or a developer hackathon, please get in touch: diy[at]artivis.net

![](http://diy.artivis.net/lib/artivis_diagram_6_site.jpg)
