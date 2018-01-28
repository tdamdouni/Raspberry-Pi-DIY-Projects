# Servo Controlled Time-Lapse Camera

_Captured: 2017-11-24 at 14:16 from [www.hackster.io](https://www.hackster.io/gotfredsen/servo-controlled-time-lapse-camera-f7d81f)_

![Servo Controlled Time-Lapse Camera](https://hackster.imgix.net/uploads/attachments/366012/img_2106_ppryWRIuNG.JPG?auto=compress%2Cformat&w=900&h=675&fit=min)

Using the **RasPi Zero** with the **PIcamera**, a **Servo** and the **OC05** Servo Driver/Controller, you can shoot a **_panning time-lapse video_**.

  * Download Raspbian Lite and unzip
  * Download Etcher and install
  * Flash Raspbian Lite to a Micro-SD card using Etcher
  * Open your terminal and go to the root of the SD Card
    
    
    cd /Volumes/boot
    echo 'dtoverlay=dwc2' >> config.txt 
    touch ssh 
    echo -n ' modules-load=dwc2,g_ether' >> cmdline.txt  
    

The last 3 lines set up the RasPi Zero (and only the Zero) to be able to [network via the USB port](http://blog.gbaman.info/?p=791). _Just verify that the last line has no newline before ' modules...' in cmdline.txt!_

  * Eject the SD Card
  * Assemble everything as per this video:

Build a Servo controlled Time-Lapse camera

  * Connect USB Cable between your RasPi Zero and your computer.
  * Either use a Mac or install **[Bonjour](https://support.apple.com/kb/DL999?viewlocale=en_US&locale=en_US)** to SSH to your RasPi Zero: `ssh pi@raspberrypi.local`
  * Password is `raspberry`
  * Finally setup internet sharing on your computer allowing **Broadcom Ethernet** to connect to your WiFi via your computer.
![](https://hackster.imgix.net/uploads/attachments/366019/screen_shot_2017-10-19_at_09_21_35_RSyARWk12E.png?auto=compress%2Cformat&w=680&h=510&fit=max)

> _Internet Sharing on a Mac_
    
    
    sudo raspi-config nonint do_expand_rootfs 
    sudo raspi-config nonint do_i2c 0 
    sudo raspi-config nonint do_camera 0 
    sudo apt-get install vim python-smbus i2c-tools 
    sudo apt-get install python-picamera python3-picamera
    sudo reboot
    

  * The first 3 lines makes full use of your SD card, activates I2C for the servo controller and activates the PIcamera.
  * Then I2C tools are getting installed and then PIcamera drivers.
  * Then reboot to make the changes take effect. 
  * Login again.
  * Test the connection to your servo controller, and if everything is fine you should see this:
    
    
    pi@raspberrypi:~ $ 
        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f 
    00:          -- -- -- -- -- -- -- -- -- -- -- -- --  
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
    70: 70 -- -- -- -- -- -- --   
    
    
    
    cd ~ 
    git clone https://github.com/xinabox/rpOC05.git  
    cd rpOC05 
    sudo python setup.py install   
    

This will install the Servo Driver library, once installed, test by:
    
    
    cd examples
    python simpletest
    

  * Copy and Paste the code below into xservo.py.
  * Create a frames directory
    
    
    cd ~
    mkdir frames
    python xservo.py
    

It should now start taking pictures and store them in frames.

  * You can have the program run automatically by `crontab -e`
  * And then write at the bottom of the file: `@reboot python /home/pi/xservo.py`
  * Once your shoot is finished, you can copy the pictures to your computer. I use `scp`
  * And then I use convert from [ImageMagick,](https://www.imagemagick.org/) like this: `convert -quality 100 frames*.jpg outputfile.mpeg`
    
    
    servo_min = 150  # Min pulse length out of 4096
    i = servo_max + 10
    filename = 'frames/frame-%s.jpg'
    pwm.set_pwm_freq(50)
    pwm.set_pwm(chan, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(chan, 0, servo_max)
    time.sleep(1)
    
      if i > servo_max:
                            
      pwm.set_pwm(chan, 0, i)
      with picamera.PiCamera(resolution=(1920,1080)) as cam:
        ts = str(datetime.utcnow())
        cam.capture(filename % ts,quality=90,thumbnail=None)
      time.sleep(0.1)
    
