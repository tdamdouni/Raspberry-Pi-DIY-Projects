# Arduino vs Raspberry Pi: Differences between the two

_Captured: 2017-05-18 at 09:51 from [circuitdigest.com](https://circuitdigest.com/article/arduino-vs-raspberryp-pi-difference-between-the-two)_

![Arduino Vs Raspberry Pi](https://circuitdigest.com/sites/default/files/field/image/Arduino-Vs-RaspberryPi.jpg)

> _Arduino Vs Raspberry Pi_

**Arduino and Raspberry Pi** are the most popular boards among the students, hobbyists and professionals. Experienced and professionals know the utility and differences between the two. But beginners and students often get confused between them, like which board to use for their project or which board is easy to learn or why should they use Arduino over Pi and vice versa. So here I am covering mostly all the aspects which make them easy to take the decision over the choice of **Arduino vs. Raspberry Pi**.

**Raspberry Pi is a fully functioned computer**, a **system-on-chip (SoC**) device, which runs on a Linux operating system specially designed for it, named **Rasbian. **Rasbian is the official OS for Raspberry Pi, where other third party OSes like Firefox OS, **Android, **RISC OS, Ubuntu Mate etc. can be installed on Pi, even **Windows 10** version is also available for Pi. Like a computer, It has memory, processor, USB ports, audio output, graphic driver for HDMI output and as it runs on Linux, most of the linux software applications can be installed on it. It has several models and revisions like Raspberry Pi, Raspberry Pi 2, Raspberry Pi Model B+ etc.

**[Arduino](http://circuitdigest.com/arduino-projects) is a microcontroller**, which is not as much powerful as Raspberry Pi, and can be considered as a one component on computer system. But it is a great hardware for electronics projects. It doesn't need any OS and software applications to run, we just need to write few lines of code to make it use. There are many Arduino boards like [Arduino UNO](http://circuitdigest.com/arduino-uno-projects), Arduino PRO, Arduino MEGA, Arduino DUE etc.

Although they are quite different but there are some similarities in terms of their inception. They both are invented in European countries, like Raspberry Pi is developed by Eben Upton in UK and Arduino is developed by Massimo Banzi in Italy. Both the inventors are teachers and they develop these hardware platforms as a design learning tool for their students. Raspberry pi was first introduced in year 2012 while Arduino in 2005.

To understand the **difference between Arduino and Raspberry Pi**, we adopted an approach where we will discuss the merits and demerits of both the hardwares over each other. So first we are starting with:

![](https://circuitdigest.com/sites/default/files/inlineimages/Arduino_uno_board.jpg)

**Simplicity:**

It's very **easy to interface analog sensors, motors** and other electronic components with Arduino, with just few lines of code. While in Raspberry pi, there is much overhead for simply reading those sensors, we need to install some libraries and softwares for interfacing these sensors and components. And the coding in Arduino is simpler, while one needs to have knowledge of Linux and its commands for using the Raspberry pi.

**Robustness:**

Raspberry Pi runs on a OS so it must be properly shut down before turning OFF the power, otherwise OS & applications may get corrupt and Pi can be damaged. While **Arduino is just a plug and play device** which can be turned ON and OFF at any point of time, without any risk of damage. It can start running the code again on resuming the power.

**Power consumption:**

Pi is a powerful hardware, it needs continuous 5v power supply and it is difficult to run it on Batteries, while **Arduino needs less power** can easily be powered using a battery pack.

**Price:**

Obviously **Arduino is cheaper** than Raspberry Pi, Arduino costs around $10-20 depending on the version, while price of Raspberry is around $35-40.

![Raspberry_Pi_B+](https://circuitdigest.com/sites/default/files/inlineimages/Raspberry_Pi_B_Plus.jpg)

One can think that Arduino is the best, after reading its merits over Raspberry Pi, but wait, it's completely depends on your project that which platform should be used. Raspberry Pi's power and its easiness is the main attraction of it, over Arduino. Below we will discuss some of its advantages over Arduino:

**Powerfulness:**

This is the main advantage of Raspberry Pi. Pi is capable of doing **multiple tasks** at a time like a computer. If anyone wants to build a complex project like an advanced robot or the project where things need to be controlled from a web page over internet then Pi is the best choice. Pi can be converted into a webserver, VPN server, print server, database server etc. Arduino is good if you just want to blink a LED but if you have hundreds of LEDs needs to be controlled over web page, then Pi is the best suited.

Raspberry **Pi is 40 times faster** than Arduino, with PI, you can send mails, listen music, play videos, run internet etc. Also as we have stated earlier that it has memory, processor, USB ports, Ethernet port etc. and it doesn't require external hardwares for most of the functions. It can be accessed **via SSH** and file can be easily transferred over **FTP**.

**Networking:**

Raspberry Pi has the **built in Ethernet port**, through which you can directly connect to the networks. Even Internet can easily be run on Pi using some USB Wi-Fi dongles. While in Arduino, it's very difficult to connect to network. External hardwares need to be connected and properly addressed using code, to run network using Arduino. External Boards called "**Shields**" needs to be plugged in, to make Arduino, as functional as Pi, with a proper coding to handle them.

**Don't need deep electronics knowledge:**

For Arduino you definitively need a electronic background, and need to know about embedded programming languages. But to start with Pi you don't need to dive into the coding languages and a small knowledge of electronics and its components is enough.

Besides those advantages, one advantage is that **OS can be easily switched** on the single Raspberry Pi board. Pi uses SD card as flash memory to install the OS, so just by swapping the memory card you can switch the operating system easily.

We can understand the need of Arduino or Pi through example. Like if you want answer any phone call automatically with a prerecorded message, then Arduino is the way. But at the same time if you want to block the robocallers or spam callers then? Then Raspberry Pi comes into picture, which can either filter the spam calls using spam callers database over the internet or it can also put a captcha type of verification for human callers.

So Arduino is suited for **repeated type of work** like open the door while anyone at the gate but Raspberry Pi can do more complex things like only open the door for authorized people. Raspberry Pi has huge potential in the world of [Internet of Things](http://circuitdigest.com/ten-examples-of-internet-of-things-iot), where machines will directly interact and control another machines, without human intervention.

### Conclusion:

Some people say that Arduino is best for beginners but I am not agree with it, a beginner can start with any one of them. Choice is just depend on your project and your background. I am concluding it with, how to make choice between these two, for your next project:

**You should choose Arduino** if:

  * You are from electronics background or if you are a beginner and really want to learn about electronics and its components.
  * Your project is simple, especially networking is not involved.
  * Your project is more like a electronics project where software applications are not involved, like Burglar alarm, voice controlled light.
  * You are not a computer geek who is not much interested in softwares and Linux.

**You should choose Raspberry Pi** If:

  * Your project is complex and networking is involved.
  * Your project is more like a software application, like a VPN server or Webserver
  * Don't have good knowledge of electronics.
  * Have good knowledge about Linux and softwares.

Although they both have their own pros and cons, but they can also be used together to make the best out of them. Like Pi can collect the data over the network and take decisions, and command the Arduino to take the proper action like rotate a motor.
