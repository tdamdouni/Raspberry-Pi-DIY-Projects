#!/usr/bin/python
#--------------------------------------
#    ___  ___  _ ____
#   / _ \/ _ \(_) __/__  __ __
#  / , _/ ___/ /\ \/ _ \/ // /
# /_/|_/_/  /_/___/ .__/\_, /
#                /_/   /___/
#
#           send_email_text.py
#  Script to send a plain text email.
#
# Author : Matt Hawkins
# Date   : 21/09/2017
#
# https://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import smtplib to provide email functions
import smtplib
 
# Import the email modules
from email.mime.text import MIMEText
 
# Define email addresses to use
addr_to   = 'user1@example.com'
addr_from = 'user2@example.com'
 
# Define SMTP email server details
smtp_server = 'mail.example.com'
smtp_user   = 'test@example.com'
smtp_pass   = '1234567889'
 
# Construct email
msg = MIMEText('This is a test email')
msg['To'] = addr_to
msg['From'] = addr_from
msg['Subject'] = 'Test Email From RPi'
 
# Send the message via an SMTP server
try:
  s = smtplib.SMTP(smtp_server)
  s.login(smtp_user,smtp_pass)
  s.sendmail(addr_from, addr_to, msg.as_string())
  s.quit()
except:
  print("There was an error sending the email. Check the smtp settings.")