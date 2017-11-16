_https://forums.pimoroni.com/t/help-building-an-pan-tilt-webinterface-for-pimoroni-pan-tilt-hat-full-kit-with-webcam-server/3654/13_

_http://your-pi-address:8082/_

```
$ sudo apt-get install libav-tools git python3-picamera python3-ws4py python3-pantilthat
$ git clone https://github.com/waveform80/pistreaming.git
$ cd pistreaming
$ git checkout pantilthat
$ python3 server.py
```
