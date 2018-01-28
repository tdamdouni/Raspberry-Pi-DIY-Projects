# Connect Raspberry Pi to cellular data network

_Captured: 2017-12-20 at 23:13 from [www.raspberrypi.org](https://www.raspberrypi.org/magpi/raspberry-pi-cellular/)_

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/12/nova-in-pi.jpg)

> _Ever wonder what your Raspberry Pi was thinking? This tutorial shows how you can ask your Pi questions no matter where it is in the world. Learn how to send questions through SMS to your Raspberry Pi and get witty answers back._

You've probably connected your Pi to the internet through Ethernet or WiFi, but have you ever considered using cellular? After all, your WiFi only covers a small portion of the planet.

This tutorial explores using cellular with the Raspberry Pi family. Hologram.io recently released the Nova, a USB modem built for single-board computers like the Pi. The Nova, Hologram's Python SDK, and Hologram's global cellular network make connecting your Pi to the mobile phone network simple.

See also:

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/12/showing-sms.jpg)

> _Connect your Pi to the mobile network and use a phone to chat to it_

You will need the [Hologram Nova](http://hologram.io/nova) which includes a free SIM.

This tutorial first appeared in The MagPi #64 and was written by Ben Strahan. Click here to download a free copy of the magazine in PDF format.

Raspberry Pi with cellular: Kit you'll need

### Raspberry Pi with cellular data: Hologram SIM configuration

Upon receiving your Nova and SIM, you need to activate the SIM to make the worldwide network available. From the [Hologram Dashboard](http://magpi.cc/2ijHyFn), click the Activate SIM button in the top right-hand corner. After activation you'll be directed to the device list page. You should see your new device in the list; it may not be clickable while it provisions onto the network.

Once the device is available, click it to be taken to the device details page. On the left you'll notice the device sub-navigation. For this tutorial we'll need to configure a device phone number and Cloud Services credentials. Select Configuration in the side-nav and walk through Configure Phone Number and Cloud Services Router sections. Make sure to save the phone number and device key for later use.

![](https://www.raspberrypi.org/magpi/wp-content/uploads/2017/12/device-activation.jpg)

> _Hologram provides instant activation and SIM management through a self-managed dashboard_

### Local Pi configuration

Next, we're going to install all the dependencies this tutorial requires. Again, Hologram makes this very simple with a single-line command. It's recommended you be connected to the internet through WiFi or Ethernet since these dependencies will use a lot of data.

On the Pi, open a Terminal window and run the following script:

`curl -L hologram.io/python-install | bash`

For this tutorial we'll need one more dependency:

`sudo apt-get install python-psutil`

You can now connect the Nova to your Pi. We'll run the following code to verify everything is installed correctly.

`sudo hologram send --cloud "Hello World!"`

Along with the Python SDK, Hologram's script installed a neat little command-line interface (CLI). Learn more about what the CLI can do by executing the following commands:

`hologram --help`  
` hologram modem --help`

Head over to the [Hologram Dashboard](http://magpi.cc/2ijHyFn) to see your 'Hello Nova' command above.

### Run SMS conversation script

Let's get the code so we can start talking with our Pi over SMS. From the Pi Terminal, clone the following repository.

`git clone https://github.com/benstr/TUT-ask-pi-sms.git`

Remember the device key you generated in the first step? Paste the device key on line 6 of the script.

`cd TUT-ask-pi-sms`  
` sudo nano askPiSMS.py`

Save the file. You're now ready to run the script and text your new robot friend, fingers crossed!

`sudo python askPiSMS.py`

From your phone, send the following questions to the phone number you received earlier.

> What is your name?  
> How old are you?  
> Do you have a body?  
> How smart are you?

By default, SMS is slow on all networks. Also, for simplicity, the code is not very fast. For both reasons, it might take 30-60 seconds to receive a response.

Congrats, you have a new robot friend you can chat with! Modify the code to support more questions or add local AI to have a truly intelligent friend.
