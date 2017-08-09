# Running A Python Script At Boot Using Cron

_Captured: 2017-05-06 at 15:57 from [www.raspberrypi-spy.co.uk](http://www.raspberrypi-spy.co.uk/2013/07/running-a-python-script-at-boot-using-cron/)_

![Crontab Example - Python at Boot](http://www.raspberrypi-spy.co.uk/wp-content/uploads/2013/07/crontab_example_02-651x336.png)

There maybe times when you want to run a Python script when your Raspberry Pi boots up. There are a number of different techniques to do this but I prefer the method that uses "cron".

Cron is a job scheduler that allows the system to perform tasks at defined times or intervals. It is a very powerful tool and useful in lots of situations. You can use it to run commands or in this case, a Python script.

## Step 1 - Create A Python Script

The first step is creating your Python script. This will be the script that will run at boot time. It is important to remember its name and location. In this example I will assume the script is called "MyScript.py" and it is located in "/home/pi/".

Double check you've got the correct path by typing :
    
    
    cat /home/pi/MyScript.py

This should show the contents of your script.

Make sure your script works and does what you expect it to. Once you are running at boot it isn't so easy to debug so don't rush!

## Step 2 - Add A New Cron Job

To create a new job to Cron we will modify the "crontab". This is a table that contains the list of jobs that Cron will monitor and run according to it's details. To edit it we use the command :
    
    
    sudo crontab -e

Each user of the system (ie "pi") can have its own Crontab but in this case we want to add it as an admin so we prefix our "crontab -e" command with "sudo". You should see something that looks like this :

Using your cursor keys scroll to the bottom and add the following line :
    
    
    @reboot python /home/pi/MyScript.py &

This tells Cron that every boot (or reboot or start-up) we want to run Python with the script MyScript.py. The "&" at the end of the line means the command is run in the background and it won't stop the system booting up as before.

Your screen should look something like this :

To save these changes click "CTRL-X", then "Y" and finally "Return". You should now be back at the command prompt.

To start testing you can now reboot using :
    
    
    sudo reboot

Once setup your Python script will run whenever your reboot or start-up your Pi. There may be times when you reboot and don't want the script running. To stop it you can find out its process number and "kill" it. To do this type :
    
    
    ps aux | grep /home/pi/MyScript.py

This should give you a line starting with "root" and ending in the path to your script. Immediately after the "root" should be a process number. For example :
    
    
    root  **1863**  0.0  1.0  24908  4012 ?  Sl  19:45  0:00  python  /home/pi/MyScript.py

In this case we can stop the process using :
    
    
    sudo kill 1863

## Final Thoughts

If you are feeling adventurous you can write your Python script to automatically exit if a certain condition is met so you don't need to ever "kill" it. Ideas include :

  * Test the GPIO pins and quit if a switch is being pressed. Maybe two switches being held down.
  * Test if a network connection is available and quit if it is. This may indicate you are testing (a camera for example) and you only want the script to auto-run when there is no network present.
  * Check for the existence of a particular file. This would allow you to create a named file to prevent the script from running at next boot.

There are other techniques to run scripts at boot up and you might want to Google "rc.local" or "init.d". I prefer the Cron method because it is so simple.

For additional information on the powerful features of Cron take a look at the [Wikipedia Cron page](https://en.wikipedia.org/wiki/Cron).
