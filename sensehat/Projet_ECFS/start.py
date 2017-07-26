# --- ECFS (Email checker for SenseHat) by Wladimir Delenclos


#--- Requis 
from sense_hat import SenseHat
from imapclient import IMAPClient
import time
import sys
from time import gmtime, strftime


# --- Parametres et configuration :
LOG = True #afficher les log dans la console 
HOSTNAME = 'imap.gmail.com' #votre serveur imap
USERNAME = 'username' #votre identifiant
PASSWORD = 'password' #votre mot de passe
MAILBOX = 'Inbox' #le dossier a veifier
NEWMAIL_OFFSET = 0   # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 20 # check mail every x seconds


# --- Demarrage 
sense = SenseHat()
sense.load_image("hello.png")

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
spinner = spinning_cursor()

print "\n\n\n############# MAIL CHECKER SYSTEM ###########"
print "#\n#"
print('# Login:  ' + USERNAME)
for _ in range(50):
    sys.stdout.write(spinner.next())
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')
try:
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)
except:
    verif = False
    print ("# Connexion impossible verifier votre configuration")
    sense.load_image("erreur.png")
else:
    verif = True
    sense.load_image("done.png")
    select_info = server.select_folder(MAILBOX)
    print("# Connexion reussie ! \n#")
    print("# Cmd+5 pour quitter ECFS")

print('#\n#')
print "#############################################\n"
time.sleep(2)

if (verif == True):
    while True:
        sense.load_image("up.png")
        folder_status = server.folder_status(MAILBOX, 'UNSEEN')
        newmails = int(folder_status['UNSEEN'])
        timeee = str(time.strftime("%H:%M:%S", gmtime()))
        
        if LOG:
            print "--->", timeee, ': ', newmails, " emails"

        if newmails > NEWMAIL_OFFSET:
            nbr = str(newmails)
            msgs = (nbr)
            sense.show_message(msgs)

            if newmails == 1:
                sense.load_image("mail.png")
            elif newmails > 1 and newmails < 15 :
                sense.load_image("mailFew.png")
            elif newmails > 14:
                sense.load_image("mailLot.png")

        else:
            sense.load_image("nomail.png")

        time.sleep(MAIL_CHECK_FREQ)

    sense.clear()
        
