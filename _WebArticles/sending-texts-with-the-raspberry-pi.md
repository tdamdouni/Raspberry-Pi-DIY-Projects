# Sending Texts with the Raspberry Pi

_Captured: 2017-05-25 at 13:40 from [hackmypi.com](https://hackmypi.com/SendTexts.php)_

![](https://hackmypi.com/images/SendTexts/TwilioLogo.jpg)

Twilio is an company that has some cool software out for sending SMS text messages from a python script. Seeing as the Pi loves python, it just makes sense to setup my Raspberry Pi to text! The ability to text will give me piece of mind during server reboots, etc. Additionally, there are a few projects in the works that will ultilize texting to send updates on things, such as motion captured by a camera (see PiCamPart1), or temperature in a room.

Twilio does allow for a trial account, however the actual costs of the service makes it a good option for makers looking to not break the bank. Head on over to Twilio.com and register an account, verify your account through your phone number, etc. Twilio will assign you a unique "account" series of letters/numbers, and a unique "token". Keep these safe, they are how you get your python programs to verify with Twilio that you have an account.

![](https://hackmypi.com/images/SendTexts/TwilioConsoleSmall.jpg)

Once your Twilio account is setup and verified through Twilio's website, it's time to send your first text! Open up a terminal window on the pi, and navigate to a folder you want to save your python scripts in. For me, I have a folder called /scripts. To create this folder, you need to run the following command:

`sudo mkdir /scripts`

Now, navigate to the folder within ther terminal with the following command:

`cd /scripts`

Once in this folder, we need to install Twilio. To do this, we are going to use python's equivelant of 'apt-get', 'pip'. Run the following command to install pip:

`sudo pip install twilio`

Modern Raspbian images come with pip by default, however if you get a '-bash' error, you may need to install pip yourself. Do that with the following command:

`sudo apt-get install python-pip`

Now that Twilio is installed, it's time to start the code. To send just a basic text with Twilio, you need 3 lines of code. So first, lets open a python script to put the code it:

`sudo nano firstText.py`

Now we have created a python script called 'firstText.py' and we are editing it, in a text editor called 'nano'. First thing we need to do is import Twilio. Doing this tells python that we intend on using Twilio, and gives us access to the Twilio library of software. Put the following line of code in the editor:

`from twilio.rest import twilioRestClient`

Next we need to authenticate with the Twilio servers. This is where the 'account' and 'token' string from earlier come in. Type the following in, putting your unique strings of characters in the correct spots:

`client = twilioRestClient(account = 'account_string' , token = 'token_string')`

Ok, so at this point we have imported Twilio, and authenticated with the servers. Now, to send our first text! The next line of code walks you through sending a single text, based on the number Twilio gave you as the from number, the number you are sending to, and the body. Notice: Twilio needs phone numbers with the country code in front, so if you want the use the number '2358675309', you will need to send it with a '+1' in the United States, so tell Twilio the number is '+12358675309'

`client.messages.create(to = '+1number' , from_ = '+1number' , body = 'Hello World')`

That's it for the code, to exit nano hit 'ctrl+x' then 'y' then 'enter'. This runs the exit command, says 'yes' to saving changes, and confirms. If everything worked correctly, type in the following command:

`sudo python firstText.py`

Give it a few seconds, and you should receive the text! If you dont, verify your "from" number is the same that Twilio assigned you, verify the "to" number, and check spelling. Other than that, python has decent error reporting, and hopefully you can debug. I can do some debugging with you if you need, but check sites like stackoverflow.com for help with that stuff first, as they are far better coders than I.

At this point, we have setup your Pi to send texts! I'll cover receiving and replying in a future guide, for sake of brevity.

#### **Parts links (as of March 2017): **

[Raspberry Pi Zero 1.3 Camera Version](https://www.amazon.com/gp/product/B01GEHPI0E/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01GEHPI0E&linkCode=as2&tag=hackmypi09-20&linkId=410902e8f3f8f1292b4a38c15153f4b6)   
[ IoT haT ](http://www.microcenter.com/product/467737/iot_hat_for_raspberry_pi)  
[ Zero LiPo ](http://www.microcenter.com/product/473055/Zero_LiPo)  
[Raspberry Pi Camera Module V2 - 8 Megapixel,1080p](https://www.amazon.com/gp/product/B01ER2SKFS/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01ER2SKFS&linkCode=as2&tag=hackmypi09-20&linkId=62525dfde014b8eefd3de12065c80c45)   
[Arducam 5 Megapixels 1080p Sensor OV5647 Mini Camera Video Module with 15 Pin 1.0mm Pitch to 22 Pin 0.5mm and 15pin to 15pin 1.0mm Ribbon Cable for Raspberry Pi Model A/B/B+, Pi 2, Pi 3 and Pi ZERO](https://www.amazon.com/gp/product/B01LY05LOE/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B01LY05LOE&linkCode=as2&tag=hackmypi09-20&linkId=c52a758db83ba305ccc0b22e07681ced)   
[SanDisk Ultra 32GB microSDHC UHS-I Card with Adapter, Grey/Red, Standard Packaging (SDSQUNC-032G-GN6MA)](https://www.amazon.com/gp/product/B010Q57T02/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B010Q57T02&linkCode=as2&tag=hackmypi09-20&linkId=cc24f60b22cf0f5137e861673b6ae76f)
