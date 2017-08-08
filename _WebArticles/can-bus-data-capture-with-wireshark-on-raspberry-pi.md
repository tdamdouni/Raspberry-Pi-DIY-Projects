# CAN-Bus Data Capture with Wireshark on Raspberry Pi

_Captured: 2017-05-11 at 22:49 from [skpang.co.uk](http://skpang.co.uk/blog/archives/1141)_

This project shows you how to setup Wireshark for use with the [PiCAN board](http://skpang.co.uk/catalog/pican-canbus-board-for-raspberry-pi-p-1196.html) to capture data on the Raspberry Pi.

Install the CAN drivers according to this:

<http://skpang.co.uk/blog/archives/1165>

Make sure the command line candump works first.

Install Wireshark
    
    
    sudo apt-get install wireshark

Bring up the CAN interface and start the GUI.
    
    
    sudo su
    
    
    ip link set can0 up type can bitrate 500000
    
    
    startx

Start Wireshark, the icon is under "Other".

![](http://www.skpang.co.uk/blog/wp-content/uploads/2014/11/wireshark4.jpeg)

Select the 1. "can0″ interface then click the 2. "Start a new live capture" icon.

![](http://www.skpang.co.uk/blog/wp-content/uploads/2014/11/wireshark5.jpeg)

> _Ensure the PiCAN is connected to an active CAN line you should see data like this:_

![](http://www.skpang.co.uk/blog/wp-content/uploads/2014/11/wireshark1.png)

> _The above capture shows a CAN ID of 7DF. Data 02 01 05 - coolant temperature request. A reply of 03 41 05 86_

![](http://www.skpang.co.uk/blog/wp-content/uploads/2014/11/IMG_4578.jpg)

### **TODO:**

It would be nice if Wireshark can decode a list of PIDs.

### **Parts List**
