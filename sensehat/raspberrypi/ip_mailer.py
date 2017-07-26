#!/usr/bin/python
# Script to email Raspberry Pi IP Address at boot using Gmail SMTP

import subprocess
import smtplib
# import socket
from email.mime.text import MIMEText
import datetime

# Change to your own account information
to = 'me@example.com'
gmail_user = 'test@gmail.com'
gmail_password = 'yourpassword'
smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_password)
today = datetime.date.today()

# Very Linux Specific
arg = 'ip route list'
p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src') + 1]
my_ip = 'ssh pi@%s' % ipaddr
msg = MIMEText(my_ip)
msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
smtpserver.sendmail(gmail_user, [to], msg.as_string())
smtpserver.quit()
