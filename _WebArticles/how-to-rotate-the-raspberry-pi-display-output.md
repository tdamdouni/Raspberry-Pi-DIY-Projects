# How to Rotate the Raspberry Pi Display Output

_Captured: 2017-11-10 at 18:49 from [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2017/11/how-to-rotate-the-raspberry-pi-display-output/#prettyPhoto)_

![Raspberry Pi 2 Model B](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2015/03/raspberry_pi_2_model_b-1078x516.jpg)

If you are building a Raspberry Project with screen there may be times you need to rotate the screen. This fairly easy to do in Raspbian.

Start by editing the config.txt file :
    
    
    sudo nano /boot/config.txt

Add one of the following lines to the bottom of the file :
    
    
    display_rotate=0
    display_rotate=1
    display_rotate=2
    display_rotate=3

0 is the normal configuration. 1 is 90 degrees. 2 is 180 degress. 3 is 270 degrees.

If you are using the Official Raspberry Pi touch screen you can use "lcd_rotate" rather than "display_rotate".

Save the file by using CTRL-X, Y then ENTER.

Then reboot using :
    
    
    sudo reboot

When the Pi restarts the display should be rotated.
