$ sudo apt-get install libav-tools git python3-picamera python3-ws4py python3-pantilthat
$ git clone https://github.com/waveform80/pistreaming.git
$ cd pistreaming
$ git checkout pantilthat
$ python3 server.py

Then once it's fired up you simply visit http://your-pi-address:8082/