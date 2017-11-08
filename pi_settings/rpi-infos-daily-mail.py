# coding=utf-8

# https://www.raspberrypi.org/forums/viewtopic.php?f=32&t=67321

import os
import smtplib
import statvfs
from datetime import timedelta
from email.mime.text import MIMEText

#Read the systems uptime:
with open('/proc/uptime', 'r') as f:
    uptime_seconds = float(f.readline().split()[0])

# At First we have to get the current CPU-Temperature with this defined function
def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()

	return(res.replace("temp=","").replace("'C\n",""))
# Now we convert our value into a float number
temp = float(getCPUtemperature())

#Read the statistics of the drives in bytes and convert to Gigabytes (using the mount points)
GB = (1024 * 1024) * 1024
USBHDD1 = os.statvfs ("/media/USBHDD1")
freeHDD1 = (USBHDD1.f_frsize * USBHDD1.f_bfree) / GB
USBHDD2 = os.statvfs ("/media/USBHDD2")
freeHDD2 = (USBHDD2.f_frsize * USBHDD2.f_bfree) / GB


# Enter your smtp Server-Connection
server = smtplib.SMTP('smtp.gmail.com', 587)
#if your using gmail: smtp.gmail.com
server.ehlo()
server.starttls()
server.ehlo
# Login
server.login("YourMail@example.com", "YourPassword")

# Now comes the Text we want to send. It will send the System Uptime, the CPU Temperature and the free space of your hard drives:
value = "System Uptime (hh:mm:ss) is: " + str(timedelta(seconds = uptime_seconds)) + "\n" + "CPU Temperature is: " + getCPUtemperature() + "C " + "\n" + "USBHDD1 Free Space: " + str(freeHDD1) + " GB" + "\n" + "USBHDD2 Free Space: " + str(freeHDD2) + " GB"
msg = MIMEText(value)
# The Subject of your E-Mail
msg['Subject'] = "Daily Raspberry Pi Status"
# Consigner of your E-Mail
msg['From'] = "Raspberry Pi"
# recipient of your E-Mail
msg['To'] = "YourMail@example.com"
# Finally send the mail
server.sendmail("Sender'sMail@example.com", "Receiver'sMail@example.com", msg.as_string())
server.quit()
Thank you very much 