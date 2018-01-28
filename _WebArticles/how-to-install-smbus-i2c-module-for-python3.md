# How to install SMBus i2c module for Python 3

_Captured: 2017-11-09 at 23:38 from [www.linuxcircle.com](http://www.linuxcircle.com/2015/05/03/how-to-install-smbus-i2c-module-for-python-3/)_

**SMBus** module worked well with Python 2, but not 3. **SMBus** is required to program i2c devices connected to Pi GPIO i2c pins such as the Raspy Juice servo controller.

**Update:**

As of the latest version of Raspbian 4.1.6 you could simply run:
    
    
    sudo apt-get update
    
    sudo apt-get install python3-smbus
    

done!

If you are not which Raspbian you are runing, run:
    
    
    uname -a

You will get something along the lines of:
    
    
    Linux raspberrypi 4.1.6-v7+ #810 SMP PREEMPT Tue Aug 18 15:32:12 BST 2015 armv7l GNU/Lin

**Older versions:**  
Here are the steps to install it:
    
    
    sudo -i
    apt-get install python3-dev
    apt-get install libi2c-dev
    cd /tmp
    wget <http://ftp.de.debian.org/debian/pool/main/i/i2c-tools/i2c-tools_3.1.0.orig.tar.bz2> # download Python 2 source
    tar xavf i2c-tools_3.1.0.orig.tar.bz2
    cd i2c-tools-3.1.0/py-smbus
    mv smbusmodule.c smbusmodule.c.orig # backup
    wget <https://gist.githubusercontent.com/sebastianludwig/c648a9e06c0dc2264fbd/raw/2b74f9e72bbdffe298ce02214be8ea1c20aa290f/smbusmodule.c> # download patched (Python 3) source
    python3 setup.py build
    python3 setup.py install
    exit
    

The next step is to enable i2c via raspi-config: _sudo raspi-config_ , select advance menu, select i2c, then enable it.

You can now try it in your Python 3 code to control your Raspy Juice or a similar device, like this:
    
    
    import smbus as smbus
    import time
    
    bus = smbus.SMBus(1)
    
    
    for i in range(1000, 2000, 100):
      bus.write_word_data(0x48, 1, i)
      time.sleep(1)
    
    bus.write_word_data(0x48, 1, 1000)
    
