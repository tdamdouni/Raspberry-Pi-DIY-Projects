#!/usr/bin/env python

from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys


recipients = ['me@gmail.com','you@yahoo.com'] 
emaillist = [elem.strip().split(',') for elem in recipients]
msg = MIMEMultipart()
msg['Subject'] = str(sys.argv[1])
msg['From'] = 'myemail@gmail.com'
msg['Reply-to'] = 'myemail@gmail.com'
 
msg.preamble = 'Multipart massage.\n'
 
part = MIMEText("Camera capture")
msg.attach(part)
 
app = open(str("../Camera/image.jpg"),"rb").read()
part = MIMEApplication(app)
part.add_header('Content-Disposition', 'attachment', filename=str("image.jpg"))
msg.attach(part)
 

server = smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login("myemail@gmail.com", "mypasswd")
 
server.sendmail(msg['From'], emaillist , msg.as_string())


