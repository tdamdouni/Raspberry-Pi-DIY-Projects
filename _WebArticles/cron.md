# CRON: What is it?

_Captured: 2017-08-24 at 23:34 from [www.tecoed.co.uk](http://www.tecoed.co.uk/cron.html)_

Cron is a utility that can be used to schedule jobs on the Raspberry Pi and its computer operating systems. You can set up and use CRON to maintain software environments or schedule jobs (commands or shell scripts) to run periodically at fixed times, dates, or intervals. This page will cover the various CRON jobs.

## Job 1: _Automatically Running a Python Program on Boot up_

1) Record where the Python program is saved, for example in the "/home/pi/" and called final.py therefore** /home/pi/final.py**

2) Double check you've got the correct path by typing :   
** sudo cat /home/pi/name_of_your_script.p**y  
_ If correct this will show the contents of your Python code._

3) Next create a **Cron **job by modifying the "crontab".

4) To edit it type **sudo crontab -e** (this will run the Cron task for **all **users)

5) Scroll to the bottom of the window and add the following line,   
**@reboot python /home/pi/**_name_of_your_program_**.py &**  
_ Don't forget the "**&**" at the end, this will run in the code in the background and the Raspberry Pi will boot up as normal._

6) Save the file using "CTRL-X", then select "Y"

7) Reboot the Pi with** sudo reboot**

To stop the program running type:  
**ps aux | grep /home/pi/name_of_your_script.py**  
This will give you the process number type:  
**Sudo kill** and the process number  
For example: **sudo kill 1867**

You can also remove the reboot code from the crontab, to stop the code from running at reboot:  
**sudo crontab -e**  
Then delete the line of code
