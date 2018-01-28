# Home Security With Raspberry Pi

_Captured: 2017-11-27 at 10:06 from [www.instructables.com](http://www.instructables.com/id/Home-Security-With-Raspberry-Pi/)_

![](https://cdn.instructables.com/FXV/PCRA/JA8JM3GT/FXVPCRAJA8JM3GT.MEDIUM.jpg)

That is a simple solution which can make you feel more relaxed when you leave your apartment - receive emails with pictures of your property being visited by unwanted guests, arm and disarm your security system the most easy and reliable way (press a switch and approach a RFID tag). And it costs nearly nothing - I pay more monthly for Internet access. You need a clone of Raspberry Pi, a few electronic parts and ... Internet access (I will soon try to write about using a GSM module).

Please note that Zoneminder is not used in this guide. If you want to use Zoneminder, have a look here:

## Step 1: Hardware You Need

![](https://cdn.instructables.com/FB8/E5CI/JA8JM2OD/FB8E5CIJA8JM2OD.MEDIUM.jpg)

1\. Raspberry Pi or its clone. The cheapest one which will suite you network access and the number of cameras you need. Don't forget to buy proper power supply with suitable connector

2\. RFID reader with antenna

3\. PIR sensor(s)

4\. a switch which connects a circuit only when you press on it (with spring?)

5\. two LEDs - green and red. Or one RGB led.

6\. two 1k resistors

7\. USB camera(s)

8\. a UTP cable to connect PIR sensors, the switch, leds and RFID reader (I have managed to connect all with one cable with 8 wires, or 4 pairs if you like)

9\. a small box or two if you want to protect your electronic parts or don't want to brag about your soldering skills.

## Step 2: Install Postfix

After having installed Linux you will need to install a few software components to run my example snippet. First you need to install Postfix if you want to send emails:

1\. **apt-get install postfix** (you will be asked to chose for example 'local only')

2\. go to **/etc/postfix** and create file **sasl_passwd** and put one line into it :

_[smtp.gmail.com]:587 john.smith:pass1234_

Replace user name and password with your credentials; you have noticed that is a line for a Google Mail account. This account is used to send alarm notifications (sent-from).

3\. **postmap hash:/etc/postfix/sasl_passwd**

4\. **rm /etc/postfix/sasl_passwd**

5\. replace the content of **/etc/postfix/main.cf **with following lines (you might want to adjust hostname):

_smtpd_banner = $myhostname ESMTP $mail_name (Ubuntu)_

_biff = no_

_append_dot_mydomain = no_

_readme_directory = no _

_smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache_

_smtp_tls_security_level = may_

_smtp_use_tls = yes_

_smtp_tls_CAfile = /etc/ssl/certs/ca-certificates.crt_

_myhostname = raspberrypi_

_myorigin = $myhostname _

_alias_maps = hash:/etc/aliases_

_alias_database = hash:/etc/aliases_

_mydestination = raspberrypi, localhost.localdomain, localhost_

_relayhost = [smtp.gmail.com]:587_

_mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128_

_mailbox_size_limit = 0_

_recipient_delimiter = +_

_inet_interfaces = all _

_smtp_sasl_auth_enable = yes_

_smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd_

_smtp_sasl_security_options =_

_smtp_sasl_tls_security_options = noanonymous_

6\. **/etc/init.d/postfix restart**

7\. you might test the configuration of Postfix by **sendmail some.name@some.address**_test content . _

## Step 3: Prepare Software 

For my Raspberry Pi B+ and Raspbian Jessie I needed to go through the following additional steps:

1\. **apt-get install python-setuptools**

2\. **easy_install pip**

3\. **pip install pyserial**

4\. **apt-get install streamer**

5\. **apt-get install mailutils**

6\. disable serial being used by console logging. I found a few different ways:

a) raspi-config -> Interfacing Options -> Serial -> Login shell NOT accessible over serial

b) removing _console=serial0,115200_ from file _/boot/cmdline.txt_

c) **systemctl stop serial-getty@ttyAMA0.service**

**systemctl disable serial-getty@ttyAMA0.service**

## Step 4: Wire It and Run It

![](https://cdn.instructables.com/FH8/FBMJ/JA8JM3KM/FH8FBMJJA8JM3KM.SMALL.jpg)

Connect your parts exactly as presented on the picture. If you don't then you will have to make changes in the source to reflect changed port numbers.

Warning! RPI IOs do not accept 5V, you should use eg TTL logic converters to decrease voltage coming from RFID or PIR sensors. It has worked for me without any damage for 2 months now maybe because of long wiring.

Ok, theoretically you could be able now to run _myalarm.py_ with:

**nohup python myalarm.py & **

But before that you need to edit the code and change IDs to your RFID tags and email address too. You can get the code here:

## Step 5: Signals in Use

![](https://cdn.instructables.com/F6Z/V3IN/JA8JMBZG/F6ZV3INJA8JMBZG.MEDIUM.gif)

## Step 6: A Few Comments at the End

A few comments to the source code, or just hints for you to write your own:

\- LEDs and PIR sensors are configured by standard GPIO.setup GPIO.OUT and GPIO.IN respectively

\- for that wiring of switch you need _GPIO.setup (**?**, GPIO.IN, pull_up_down=GPIO.PUD_UP)_

\- the RFID reader is connected to GPIO15 which is board's RX, this can be read with

_ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=0.1) and ser.read(12)_

This works on Raspbian Jessie on RPI 1, but it might be changed to _/dev/serial0 _with other distributions.

\- maybe there should be a resistor for the switch too

\- I use _streamer _to dump images from USB cameras:

**streamer -c /dev/video0 -s 640x480 -o camdmp.jpeg**

and **streamer -c /dev/video1 -s 640x480 -o camdmp2.jpeg** for the second camera

\- write some alarming wake-up text into _alarmmsg.txt_ file and send email with:

**mail -s "Alarm" -t john.smith@gmail.com -A camdmp.jpeg -A camdmp2.jpeg < alarmmsg.txt**

Have fun!

## Comments
