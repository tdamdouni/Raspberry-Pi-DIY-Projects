# Raspberry Pi Smart Car

_Captured: 2018-06-29 at 08:22 from [www.hackster.io](https://www.hackster.io/tinkernut/raspberry-pi-smart-car-8641ca?utm_source=Hackster.io+newsletter&utm_campaign=7d901795d1-EMAIL_CAMPAIGN_2017_07_26_COPY_01&utm_medium=email&utm_term=0_6ff81e3e5b-7d901795d1-141949901&mc_cid=7d901795d1&mc_eid=1c68da4188)_

![Raspberry Pi Smart Car](https://hackster.imgix.net/uploads/attachments/507608/mvi_6389_mp4_00_00_20_05_still001_U35d3qOmSw.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

I love the idea of smart cars, but it's hard for me to justify purchasing a whole new car just to get a couple of bells and whistles. For the time being, I'm stuck with my "dumb" car, but that doesn't mean I can't try and make it smarter myself!

![](https://hackster.imgix.net/uploads/attachments/507980/tesla_fdCtTrWnKL.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

The term "Smart Car" can have dozens of different meanings depending on who you ask. So let's start with my definition of a smart cart:

  * Touchscreen interafce
  * Backup camera that let's you know if an object is too close
  * Basic information about the car, such as fuel efficiency
  * Maybe bluetooth connectivity?

I'm not sure which, if any, of those items I'll have any success with, but I guess we'll find out.

The first obvious addition to our smart car wannabe is a backup camera. There are many kits out there that makes adding a backup camera pretty simple. But most of them require making modifications to the car itself, and since I'm just wanting to test a proof of concept, I don't really want to start unscrewing and drilling into my car.

![](https://hackster.imgix.net/uploads/attachments/507988/s-l300_5e6YEtgdXU.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

![](https://hackster.imgix.net/uploads/attachments/507992/still01_szOukmbq7Q.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

One caveat with cameras like these is that they require and external power source. Generally it's prescribed to wire them to one of the reverse lights of your car so that it's automatically powered on when the car is in reverse. Being that I don't want to modify my car at this time, I'm just going to wire it up to some batteries. And I'll mount it to the license plate using trusty old duct tape!

;

;

![](https://hackster.imgix.net/uploads/attachments/507999/step02_AfhRywbsJd.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

I ran an RCA cable from the camera to the dashboard and connected it to my 5' LCD. This specific LCD can be powered through USB, so I plugged it in to a USB lighter adapter (most old cars have lighter adapters).

;

;

![](https://hackster.imgix.net/uploads/attachments/508031/step05_C3Zkuyzifu.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

After starting the car, the screen immediately came on and I could see the image from the camera. Works as advertised! This would be a good solution for anyone just wanting to add a backup camera to their car, and don't want any bells and whistles with it. I think I can do better, however.

![](https://hackster.imgix.net/uploads/attachments/508032/step06_h3cYvHjvbn.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Enter the Raspberry Pi. The Pi is the perfect platform for a smart car, because it's basically a mini computer with tons of inputs and outputs. When connecting a camera to the Pi, you can use practically any generic USB webcam, or you can go with [Pi Camera](https://amzn.to/2MPTM3p). Neither camera requires a separate power source. But just make sure you have plenty of cable to go to the back of the car.

;

;

![](https://hackster.imgix.net/uploads/attachments/508034/step07_xNEJ8Sx5BH.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

I opted for the Pi Camera because it has higher throughput than a USB camera. Again, I just duct taped the camera to the license plate, ran the flat cable to the Pi at the front of the car, and then connected it to a 7" touchscreen. Both the Pi and the touchscreen can be powered by the USB adapter in the car.

;

;

![](https://hackster.imgix.net/uploads/attachments/508040/step08_Qooal6LnGU.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Turning on the car, both the Pi and the screen powered up. One obvious downside is the boot time required for the Pi to boot up...something I'll have to consider later. To view the Pi cam, I opened up the terminal and ran a simple script (a script that can be set to auto-boot in the future)
    
    
    raspivid -t 0
    

or
    
    
    raspivid -t 0 --mode 7
    

After hitting enter, a feed of the video camera popped up! The nice thing about video on the Pi is that you can analyze it, and maybe even set up an alert system if an object gets too close! Keep an eye on this project page to see if I'm able to do just that!

![](https://hackster.imgix.net/uploads/attachments/508047/step14_OCFPHBVsNN.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)
