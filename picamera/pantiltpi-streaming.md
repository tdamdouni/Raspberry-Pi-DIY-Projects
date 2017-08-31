_http://forums.pimoroni.com/t/help-building-an-pan-tilt-webinterface-for-pimoroni-pan-tilt-hat-full-kit-with-webcam-server/3654_

_https://github.com/waveform80/pistreaming/tree/pantilthat_

```
$ sudo apt-get install libav-tools git python3-picamera python3-ws4py python3-pantilthat
$ git clone https://github.com/waveform80/pistreaming.git
$ cd pistreaming
$ git checkout pantilthat
$ python3 server.py
```

Then once it's fired up you simply visit http://your-pi-address:8082/4 and you should see the (crude) interface. As for the complete code - it's all in the repo - nothing hidden. If you've got any specific questions about the code, I'm happy to try and answer them.

```
cd pistreaming
git diff
```

```
git reset --hard
```
