# Projet_ECFS Email checker for SenseHat (Raspberry Pi 3)

A notification and check system for gmail on **Raspberry Pi 3** & **Sense Hat**.
The aim is to use the Sense Hat module as notifier , of the state of your inbox.
It works perfectly with **Gmail** and **Inbox by Google**. 
Nevertheless, it is theoretically compatible with **all email server using IMAP** without advanced connection (other than Login / Password).



_______



## Requiered

ECFS, Email checker for SenseHat Raspberry Pi 3 **require**:

+ A _Raspberry Pi_ (v.3b recommanded)
+ A _SenseHat_ 
+ Python 2.7
  + SenseHat
  + IMAPClient
+ Nano (for configuration)

_______

## Install

Pull or exctract the repository where you whant on your rapsberry.

#### Install required elements
Open your command line and, before launch any script, install the following python libraries and apt: 

    pip install imapclient
    sudo apt-get update
    sudo apt-get install sense-hat
    sudo reboot
    
    
#### Settings
Now, you can configure ECFS (currently the comments are in french because i'm french) :

    sudo nano start.py
    
    
Find the followings required variables and put your own values in: 

    HOSTNAME = 'imap.gmail.com' 
    USERNAME = 'username'
    PASSWORD = 'password' 
    

##### Optional 
You can also modify some other values like :
 
 If you want show logs in the terminal:
 
     LOG = True 
     
 Choose the folders to modify:
 
     MAILBOX = 'Inbox'
     
 check mail every x seconds:
 
     MAIL_CHECK_FREQ = 20

#### Start
    python start.py

_______

## How it's work ? 

ECFS have a simple userflow.

After the loading icon ![Icones](https://github.com/wladouche/Projet_ECFS/blob/master/hello.png), you have two feedbacks, ![Icones](https://github.com/wladouche/Projet_ECFS/blob/master/erreur.png) or  ![Icones](https://github.com/wladouche/Projet_ECFS/blob/master/done.png). If you see the red cross, you have a problem, check your config values. 
If not, perfect, the terminal must show a congratulation message. 

At this moment, some possibilities : 

 - ![Icones](https://github.com/wladouche/Projet_ECFS/blob/master/mail.png) -> *Green* You have one mail
 - ![Icones](https://github.com/wladouche/Projet_ECFS/blob/master/mailFew.png) -> *Yellow* You have more than 1 mail and less than 14 mails
 - ![Icones](https://github.com/wladouche/Projet_ECFS/blob/master/mailLot.png) -> *red* You have more than 15 mails

In this 3 cases, each X seconds specified in the MAIL_CHECK_FREQ value you have the right number of mails. 
 
 - ![Icones](https://github.com/wladouche/Projet_ECFS/blob/master/nomail.png) -> You dont have mails (smiley happy ! ) 
 - ![Icones](https://github.com/wladouche/Projet_ECFS/blob/master/up.png) -> During a checkup


Enjoy ! 
