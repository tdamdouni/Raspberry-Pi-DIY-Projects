# Send Text and HTML Email Using Python on the Raspberry Pi

_Captured: 2017-09-23 at 12:29 from [www.raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2012/05/send-text-and-html-email-using-python/?utm_content=bufferc01fb&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer)_

![Raspberry Pi Python](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/08/raspberry_pi_python-1078x516.jpg)

My first attempt at Python programming was a script to send email. This is something I planned to use in a future applications so I thought it was a good first step.

## Sending Plain Text Email

The first script shown below sends a basic plain text email to a specified email address. You need to enter the details of your SMTP server :

1234567891011121314151617181920212223242526272829
`# Import smtplib to provide email functions``import` `smtplib``# Import the email modules``from` `email.mime.text ``import` `MIMEText``# Define email addresses to use``addr_to   ``=` `'user1@example.com'``addr_from ``=` `'user2@example.com'``# Define SMTP email server details``smtp_server ``=` `'mail.example.com'``smtp_user   ``=` `'test@example.com'``smtp_pass   ``=` `'1234567889'``# Construct email``msg ``=` `MIMEText(``'This is a test email'``)``msg[``'To'``] ``=` `addr_to``msg[``'From'``] ``=` `addr_from``msg[``'Subject'``] ``=` `'Test Email From RPi'``# Send the message via an SMTP server``try``:``s ``=` `smtplib.SMTP(smtp_server)``s.login(smtp_user,smtp_pass)``s.sendmail(addr_from, addr_to, msg.as_string())``s.quit()``except``:``print``(``"There was an error sending the email. Check the smtp settings."``)`

It can be run from the command line using :
    
    
    python send_email_text.py

or :
    
    
    python3 send_email_text.py

You can download this script directly to your Pi using :
    
    
    wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/send_email_text.py

## Sending HTML Email

The script below is similar but it sends an HTML formatted email. You can also specify plain text which would be read by a email client that could not read the HTML version.

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152
`# Import smtplib to provide email functions``import` `smtplib``# Import the email modules``from` `email.mime.multipart ``import` `MIMEMultipart``from` `email.mime.text ``import` `MIMEText``# Define email addresses to use``addr_to   ``=` `'user1@example.com'``addr_from ``=` `'user2@example.com'``# Define SMTP email server details``smtp_server ``=` `'mail.example.com'``smtp_user   ``=` `'test@example.com'``smtp_pass   ``=` `'1234567889'``# Construct email``msg ``=` `MIMEMultipart(``'alternative'``)``msg[``'To'``] ``=` `addr_to``msg[``'From'``] ``=` `addr_from``msg[``'Subject'``] ``=` `'Test Email From RPi'``# Create the body of the message (a plain-text and an HTML version).``text ``=` `"This is a test message.\nText and html."``html ``=` `"""\``<html>``<head></head>``<body>``<p>This is a test message.</p>``<p>Text and HTML</p>``</body>``</html>``"""``# Record the MIME types of both parts - text/plain and text/html.``part1 ``=` `MIMEText(text, ``'plain'``)``part2 ``=` `MIMEText(html, ``'html'``)``# Attach parts into message container.``# According to RFC 2046, the last part of a multipart message, in this case``# the HTML message, is best and preferred.``msg.attach(part1)``msg.attach(part2)``# Send the message via an SMTP server``try``:``s ``=` `smtplib.SMTP(smtp_server)``s.login(smtp_user,smtp_pass)``s.sendmail(addr_from, addr_to, msg.as_string())``s.quit()``except``:``print``(``"There was an error sending the email. Check the smtp settings."``)`

The script constructs a multi-part message where each part contains either the plain text or HTML versions of the message.

You can download this script directly to your Pi using :
    
    
    wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/send_email_html.py

Hopefully these basic examples are enough to get you started.
