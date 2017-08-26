# Who-is-hogging-the-Internet?
A Raspberry Pi project to search and find who is using an Internet connection

If like, me you live in a house which contains several other people and their numerous devices then you may well be used to others hogging the Internet connection.  This project was  designed to monitor who was on the Internet and which devices are connected.  
The concept is simple, 
* 1. Scan the Network for devices
* 2. Pull out the name of the devices
* 3. Compare with a list of stored devices
* 4. If they match then announce the device is connected
* 5. Light up a corresponding LED on the Blinkt
* 6. If a devices disconnects turn he LED off and provide and audio message

The project uses NMAP which is 'Nmap (Network Mapper) is a security scanner used to discover hosts and services on a computer network, thus creating a "map" of the network. 

#Load the LX Terminal:
sudo apt-get install nmap

pip install python3-nmap

sudo apt-get install espeak python-espeak

# Simple usage is:
import nmap

nm = nmap.PortScanner()

data = nm.scan(hosts="192.168.1.1/24", arguments="-sP")

print (data['scan'])

[Project Website](http://www.tecoed.co.uk/blinkt.html)

[YouTube Video](https://www.youtube.com/watch?v=r_JDw65FTMA&feature=youtu.be)
