# Play With Raspberry Pi ZERO and PHat

_Captured: 2017-09-15 at 10:13 from [www.hackster.io](https://www.hackster.io/masteruan/play-with-raspberry-pi-zero-and-phat-140b9a)_

![Play With Raspberry Pi ZERO and PHat](https://hackster.imgix.net/uploads/attachments/262189/FO6FD8KIW6PT740.LARGE.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

;

;

![](https://hackster.imgix.net/uploads/attachments/262176/FJ14P4GIW6PT220.LARGE.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

Raspberry Pi zero is a smallest version of Raspberry Pi. The Raspberry Pi is not a comestible kind, but is a Microcomputer. A single board computer that have CPU, RAM, HD, all connections like USB, HDMI etc.

I have also discovered a small led matrix 11x5 by [Pimoroni](https://shop.pimoroni.com/), the [pHat](http://amzn.to/2gDyOqI). This is a small and pretty led matrix that with this little pretty Raspberry Pi, the Raspberry Pi zero, make a very kindly object. A led scrolling led matrix, that you can program in Python.

I show you where to buy the Raspberry Pi, where buy the pHat, and how to install the library and the code for work with the pHat matrix.

**On Amazon you can buy the**

**The Raspberry Pi Zero is available only on Pimoroni**

;

;

![](https://hackster.imgix.net/uploads/attachments/262181/FM3UXXYIW6PQYMU.LARGE.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

After the soldering step, you can connect the pHat to your Raspberry Pi zero.

In the **Terminal** window, type:
    
    
    sudo raspi-config
    

put the password (default is raspberry)

1\. Go to Advanced Options

2\. Select I2C

3\. Enable the I2C port

Open a Terminal and type:
    
    
    sudo pip3 install scrollphat
    

or
    
    
    sudo apt-get install python3-scrollphat
    

Open a Terminal and type:
    
    
    sudo pip2 install scrollphat
    

or
    
    
    sudo apt-get install python-scrollphat
    

;

;

![](https://hackster.imgix.net/uploads/attachments/262183/FYGWM9SIW6PT21H.LARGE.jpg?auto=compress%2Cformat&w=680&h=510&fit=max)

You can download the three files on your Raspberry Pi. The graph file generate a random lines on your pHat, the tempCpu, show the CPU temperature of your Raspberry Pi zero, and the meteoShare.py show the local meteo condition.

If you want use meteo file you must install the pyown library by terminal:
    
    
    sudo pip install pyown
    

After you must provide a valid API key by using pyown library. The weather service you're going to use in this resource is called OpenWeatherMap. It's a completely free service, and has an easy-to-use API. You're going to need your own account though, so click on the link to go to the website: [http://openweathermap.org](http://openweathermap.org/)

![](https://hackster.imgix.net/uploads/attachments/262186/FQBNSXEIW6PT76L.ANIMATED.LARGE.gif?auto=compress%2Cformat&w=680&h=510&fit=max)

In the Terminal window, go to the same folder where are graph.py file, and type:
    
    
    python graph.py
    

or
    
    
    python3 cpuTemp.py
    

or
    
    
    python meteoShare.py
    

**See the result!**
