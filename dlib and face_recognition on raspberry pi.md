# Install dlib and face_recognition on a Raspberry Pi

Instructions tested with a Raspberry Pi 2 with an 8GB memory card. Probably also works fine on a Raspberry Pi 3.

## Steps

Download the [latest `Raspbian Jessie Light` image](https://www.raspberrypi.org/downloads/raspbian/). Earlier versions of Raspbian won't work.

Write it to a memory card using [Etcher](https://etcher.io/), put the memory card in the RPi and boot it up. 

Log in. Default username / password is `pi` / `raspberry`.

Set up Wifi (if you are using Wifi) [according to the Raspberry Pi instructions](https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md).

Run `sudo raspi-config` and configure the basics:
- Set up your keyboard layout (It defaults to a British keyboard layout)
- Change default user password
- Enable the Raspberry Pi camera (if you have one attached)
- Configure gpu memory split under 'Advanced'. Set it up '16'.
- Save changes and reboot.

Install required libraries with these commands:
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    python3-pip \
    zip
sudo apt-get clean
```

Install the picamera python library with array support (if you are using a camera):
```
sudo apt-get install python3-picamera
sudo pip3 install --upgrade picamera[array]
```

Temporarily enable a larger swap file size (so the dlib compile won't fail due to limited memory):
```
sudo nano /etc/dphys-swapfile

< change CONF_SWAPSIZE=100 to CONF_SWAPSIZE=1024 and save / exit nano >

sudo /etc/init.d/dphys-swapfile restart
```

Download and install dlib v19.6:
```
mkdir -p dlib
git clone -b 'v19.6' --single-branch https://github.com/davisking/dlib.git dlib/
cd ./dlib
sudo python3 setup.py install --compiler-flags "-mfpu=neon"
```

Install `face_recognition`:
```
sudo pip3 install face_recognition
```

Revert the swap file size change now that dlib is installed:
```
sudo nano /etc/dphys-swapfile

< change CONF_SWAPSIZE=1024 to CONF_SWAPSIZE=100 and save / exit nano >

sudo /etc/init.d/dphys-swapfile restart
```

Download the face recognition code examples:
```
git clone --single-branch https://github.com/ageitgey/face_recognition.git
cd ./face_recognition/examples
python3 facerec_on_raspberry_pi.py
```

Totally Optional: If you want a desktop GUI, install PIXEL:

```
sudo apt-get install --no-install-recommends xserver-xorg xinit raspberrypi-ui-mods
```