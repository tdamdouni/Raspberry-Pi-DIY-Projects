from threading import Thread
import requests ## pip install requests
import time
import smtplib

## email sending function
def email_sender(input_message, email_to, client):
	''' function to send email '''
	to = email_to
	gmail_user = '' ## email of sender account
	gmail_pwd = '' ## password of sender account
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo
	smtpserver.login(gmail_user, gmail_pwd)
	header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:site down! \n'
	input_message = input_message + client
	msg = header + input_message
	smtpserver.sendmail(gmail_user, to, msg)
	smtpserver.close()

## list of sites to track along with email address to send the alert
clients = {
	"http://www.hecasecentre.org/educators":"mike@recantha.co.uk"
}

## temporary dictionary used to do separate monitoring when a site is down
temp_dic = {}

## site 'up' function
def site_up():
	''' function to monitor up time '''
	while True:
		for client, email in clients.items():
			try:
				r = requests.get(client)
				if r.status_code == 200:
					print client, 'Site ok'
					time.sleep(60) ## sleep for 1 min
				else:
					print client, 'Site first registered as down - added to the "site down" monitoring'
					temp_dic[client]=email
					del clients[client]
			except requests.ConnectionError:
				print client, 'Site first registered as down - added to the "site down" monitoring'
				temp_dic[client]=email
				del clients[client]

## site 'down' function
def site_down():
	''' function to monitor site down time '''
	while True:
		time.sleep(900) ## sleeps 15 mins
		for client, email in temp_dic.items():
			try:
				r = requests.get(client)
				if r.status_code == 200:
					print client, 'Site is back up!!'
					email_sender('Site back up!! ', email, client)
					clients[client]=email
					del temp_dic[client]
				else:
					email_sender('Site down!! ', email, client)
					print client, 'Site Currently down - email sent'
			except requests.ConnectionError:
				email_sender('Site down!! ', email, client)
				print client, 'Site Currently down - email sent'
			
t1 = Thread(target = site_up)
t2 = Thread(target = site_down)
t1.start()
t2.start()
