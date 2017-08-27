# SMART HOME SECURITY SYSTEM

_Captured: 2017-08-25 at 09:59 from [www.hackster.io](https://www.hackster.io/mtechkiran/smart-home-security-system-43016f)_

![SMART HOME SECURITY SYSTEM](https://hackster.imgix.net/uploads/attachments/304926/untitled_yXsnTUXk7p.jpg?auto=compress%2Cformat&w=900&h=675&fit=min)

In today's era, home security is becoming increasingly prominent feature. Security is primary concern everywhere and for everyone. Every person wants his home, industry etc. to be secured. The aim of our project is to design and implement affordable, flexible and fast monitoring home security system using a Raspberry Pi and a Passive Infrared (PIR) motion sensor. In this project we use motion detection to trigger video recording via the Raspberry Pi camera module.

A Passive Infrared (PIR) sensor interfaced to the Raspberry Pi which detects when a human (or any animal) moves in front of it, and signals this detection to the Raspberry Pi. The Raspberry Pi than triggers the video recording via the Raspberry Pi Camera module. Meantime the notification about the detection will be sent to us via an email. Once a notification is received, we can log into our Raspberry Pi remotely and view the recorded video and if found something theft is going to happen we can raise an alarm through an active buzzer to intimate others and hence we can secure our home.

![Untitled iddtenjwiv](https://halckemy.s3.amazonaws.com/uploads/attachments/304930/untitled_idDTENJwiV.jpg)
    
    
    
        recipients = ['mtech.kiran@gmail.com']
        
        outer['Subject'] = 'mail'
        outer['To'] = COMMASPACE.join(recipients)
        outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    
        attachments = ['/home/pi/image/image1.jpg']
    
        for file in attachments:
                with open(file, 'rb') as fp:
                    msg = MIMEBase('application', "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                outer.attach(msg)
                print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
    
        composed = outer.as_string()
    
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.login(sender, gmail_password)
                s.sendmail(sender, recipients, composed)
            print("Unable to send the email. Error: ", sys.exc_info()[0])
    
    
        camera.capture('/home/pi/image/image1.jpg')
        filename = datetime.now().strftime("/home/pi/videos/%Y-%m-%d_%H.%M.%S.h264")
    
