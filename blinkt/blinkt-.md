
__ __ __ __

* * *

## What is it?

* * *

**[Pimoroni](https://shop.pimoroni.com/products/blinkt)** have created an awesome eight super-bright RGB LED indicator which is ideal for adding visual notifications to your Raspberry Pi without breaking the bank!  The Blinkt!  Inspired by Alex Ellis's work with his Raspberry Pi Zero Docker Cluster they developed the boards for him to use as status indicators. They offer eight APA102 pixels in the smallest (and cheapest) form factor to plug straight into your Raspberry Pi 3/2/B+/A+/Zero.

* * *

## 1 Install the Library

* * *

The guys at Pimoroni have made it very easy toinstall the software for your Blinkt! and it also comes with a wide selection of cool examples to show off the features of the Blinkt!    
  
**Open the LX Terminal and type: **  
**curl -sS get.pimoroni.com/blinkt | bash**  
You will find all the examples in the folder /home/pi/Pimoroni/blinkt.  
  
**Set an LED with the code:**  
from blinkt import set_pixel, show  
set_pixel(0,255,0,0) show()  
  
**Adjust the brightness with:**  
from blinkt import set_brightness  
set_brightness(0.5)  
  
That is how simple it is!

* * *

## Who is hogging the Internet?

* * *

If like, me you live in a house which contains several other people then you may well be used to others hogging the Internet connection.  This project was  designed to monitor who was on the Internet and which devices are connected.  The concept is simple, 

  1. _Scan the Network for devices_
  2. _Pull out the name of the devices_
  3. _Compare with a list of stored devices_
  4. _If they match then announce the device is connected_
  5. _Light up a corresponding LED on the BlinkT_
  6. _If a devices disconnects turn he LED off and provide and audio message_

* * *

## 1\. Getting Set up

* * *

The project uses NMAP which is 'Nmap (Network Mapper) is a security scanner used to discover hosts and services on a computer network, thus creating a "map" of the network. To accomplish its goal, Nmap sends specially crafted packets to the target host and then analyzes the responses.'   Install a Python module which enables you to control Nmap with Python code,    
  
**Load the LX Terminal:**  
_**sudo apt-get install nmap**  
**pip install python3-nmap**_  
  
Further details can be found[ here](http://xael.org/pages/python-nmap-en.html)

* * *

## 2\. Finding Devices

* * *

Nmap makes it nice and easy to scan the devices that are connected to your Hub. Ensure that your Pi is connected and then open Python adding the program below, this will scan and return a list of devices, including the name, IP address, whether it is connected and more.  
  
_** nm = nmap.PortScanner()  
 data = nm.scan(hosts="192.168.1.1/24", arguments="-sP")  
 print (data['scan'])**_

* * *

## 3\. Splitting the Data

* * *

Now you have the data about the devices you can use some Python string manipulation to extract the required information and values.  First convert the data into a string and then split is at the { symbol.  
​  
_**text = str(data['scan'])  
text = text.split("{")  
ip_find = 'hostname'**_  
  
For each of the entries in the text string find the word hostname and then end of the word, it ends with a space so it is easy to find.  This will locate the name if the device, for example, 'iPhone' or ' Raspberry Pi'.   After it has found each device name it adds them to a list called final devices.  This is used to compare with a pre set list of allowed devices as well as work out if the device is online or off line.  
  
_**###finds the names of the devices###  
  for i in text:  
      if ip_find in i:  
          ##find the name of the device###   
          start = i.find("hostname")  
          end = i.find(".default")  
          final = i[start+12:end]  
          final_devices.append(final)  
           
    final_devices = str(final_devices)  
    print (final_devic**_es).

## Who is in?

* * *
* * *

## 4\. Responding to on / off line devices

* * *

Now respond to whether or not a particular device has been found, in this example the Raspberry Pi.  If it is found then turn on the corresponding Blinkt LED​.  Update the device status into the list so that you can check if the devices has come on line or gone offline, see the next step.   
  
If the device is not found then set the LED to a value of (0,0,0) which turns of the LED indicator.  Set the status value of the device to 0 indicating that it is off, or offline.  
  
_**if final_devices.find("raspberrypi") != -1:  
        print ("Pi Found")  
        set_pixel(1,255,150,0)  
        show()  
        if device_status2[1] == 0:    #check status is 0 and then update to 1  
            device_status2[1] = 1  
        else:  
            pass  
    else:  
        set_pixel(1,0,0,0)  
        show()  
        if device_status2[1] == 1:  
            device_status2[1] = 0  
        else:  
            pass**_ 

* * *

## 5\. Is the Device Online or Offline

* * *

The last section of the program checks whether devices are online or offline and announces it to the user.  This is easy but because a loop is used each minute to check the status, the program will keep announcing the devices that are online.  This becomes annoying after a while.  Better that the program only announces a change in state, for example a device comes on line or goes off line.   This is done using two lists.  The first stores a value of either 1 or 0 for a device being on or off.  Each device is assigned a position in the list, so the Raspberry Pi is position 1.  Then in step four when the Namp scans for connected devices, the values are added to a new lists.  Then the two lists are compared to find any changes.  
  
_**for i in device_status2:  
        if i == device_status[x]:  
            print (i)  
            print ("same")  
            x = x + 1  
              
        elif i != device_status[x]:  
            print (i)  
            print (type(i))  
            print ("change")  
            print ("Number", x, "changed")**_  

   
A dictionary stores the postion of each device and also the 'message' which is to be annonced, for example, "Dan's phone is online" or "Dan's phone is offline".   
           

_**            x = str(x)  
            ####check for changes and pull out voice annoucement#####  
            if i == 0:  
                #print ("went off")  
                print (Dictionary_Offline[x])  
                espeak.synth(Dictionary_Offline[x])  
                time.sleep(1.5)  
            elif i == 1:  
                #print ("Went on")  
                print (Dictionary_Online[x])  
                espeak.synth(Dictionary_Online[x])   
                time.sleep(1.5)  
            x = int(x)  
            x = x + 1  

  
    device_status = device_status2**_

* * *

