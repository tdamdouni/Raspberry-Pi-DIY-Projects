#!/usr/bin/env bash
# Customize New Ubuntu on Raspberry Pi

# YOU MUST SET THESE VARIABLES FIRST
id_rsa_pub="YOUR SSH PUB KEY"
wep_wifi_ssid="YOUR WEP WIFI SSID"
wep_wifi_password="YOUR WEP WIFI PASSWORD"
gmail_user="YOUR GMAIL EMAIL ADDRESS"
gmail_password="YOUR GMAIL PASSWORD"
email_to="EMAIL RECIPIENT"


# Pause
function pause(){
	read -p "Press any key to continue..."
	echo
}

# Warning
echo "##################################################################"
echo "This script will setup a new Raspberry Pi with Raspbian installed."
echo "You should not proceed if you have already modified some settings,"
echo "Or if you have not configured the required variables in this file."
echo "##################################################################"
echo
pause

# Check Variables Set
if [ "$id_rsa_pub" = "YOUR SSH PUB KEY" ]; then
	echo "You failed to configure the variables!"
	echo "Please edit this script before running."
	exit 1
fi


# PACKAGE UPDATES AND INSTALLATIONS
sudo apt-get update
sudo apt-get install -y git ImageMagick openssh-server wireless-tools wpasupplicant python-setuptools cmake libssl-dev --force-yes
sudo easy_install pip
sudo apt-get upgrade -y


# CONFIG NETWORKING
sudo sed -i 's/manual/dhcp/' /etc/network/interfaces


# CONFIG WIFI
touch /etc/wpa_supplicant/wpa_supplicant.conf
bash -c 'echo >> /etc/wpa_supplicant/wpa_supplicant.conf'
bash -c 'echo "network={" >> /etc/wpa_supplicant/wpa_supplicant.conf'
bash -c 'echo "        ssid=\"REPLACE1\"" >> /etc/wpa_supplicant/wpa_supplicant.conf'
bash -c 'echo "        psk=\"REPLACE2\"" >> /etc/wpa_supplicant/wpa_supplicant.conf'
bash -c 'echo "}" >> /etc/wpa_supplicant/wpa_supplicant.conf'
bash -c 'echo >> /etc/wpa_supplicant/wpa_supplicant.conf'
sed -i "s/REPLACE1/$wep_wifi_ssid/" /etc/wpa_supplicant/wpa_supplicant.conf
sed -i "s/REPLACE2/$wep_wifi_password/" /etc/wpa_supplicant/wpa_supplicant.conf

ifconfig wlan0 down
ifconfig wlan0 up
# iwconfig
# iwlist scan
# wpa_passphrase 


/etc/network/interfaces

# SSH
mkdir ~/.ssh
touch ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
echo $id_rsa_pub >> ~/.ssh/authorized_keys
echo >> ~/.ssh/authorized_keys


# SSHD CONFIG
sudo bash -c 'echo >> /etc/ssh/sshd_config'
sudo bash -c 'echo >> /etc/ssh/sshd_config'
sudo bash -c 'echo "Match User ubuntu" >> /etc/ssh/sshd_config'
sudo bash -c 'echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config'
sudo bash -c 'echo "RSAAuthentication yes" >> /etc/ssh/sshd_config'
sudo bash -c 'echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config'
sudo bash -c 'echo >> /etc/ssh/sshd_config'
sudo bash -c 'echo "Match User root" >> /etc/ssh/sshd_config'
sudo bash -c 'echo "PasswordAuthentication no" >> /etc/ssh/sshd_config'


# BASHRC
echo >> ~/.bashrc
echo "export CLICOLOR=1" >> ~/.bashrc
echo "export LSCOLORS=eafxcxdxbxegedabagacad" >> ~/.bashrc
echo "export GREP_OPTIONS='--color=auto'" >> ~/.bashrc
echo >> ~/.bashrc
echo "alias ll='ls -lah --color'" >> ~/.bashrc
source ~/.bashrc


# IP MAILER
touch ~/ip_mailer.py
chmod +x ~/ip_mailer.py

echo "#!/usr/bin/python" >> ~/ip_mailer.py
echo "# Script to email Raspberry Pi IP Address at boot using Gmail SMTP" >> ~/ip_mailer.py
echo "" >> ~/ip_mailer.py
echo "import subprocess" >> ~/ip_mailer.py
echo "import smtplib" >> ~/ip_mailer.py
echo "from email.mime.text import MIMEText" >> ~/ip_mailer.py
echo "import datetime" >> ~/ip_mailer.py
echo "" >> ~/ip_mailer.py
echo "# Change to your own account information" >> ~/ip_mailer.py
echo "to = '$email_to'" >> ~/ip_mailer.py
echo "gmail_user = '$gmail_user'" >> ~/ip_mailer.py
echo "gmail_password = '$gmail_password'" >> ~/ip_mailer.py
echo "smtpserver = smtplib.SMTP('smtp.gmail.com', 587)" >> ~/ip_mailer.py
echo "smtpserver.ehlo()" >> ~/ip_mailer.py
echo "smtpserver.starttls()" >> ~/ip_mailer.py
echo "smtpserver.ehlo" >> ~/ip_mailer.py
echo "smtpserver.login(gmail_user, gmail_password)" >> ~/ip_mailer.py
echo "today = datetime.date.today()" >> ~/ip_mailer.py
echo "" >> ~/ip_mailer.py
echo "# Very Linux Specific" >> ~/ip_mailer.py
echo "arg = 'ip route list'" >> ~/ip_mailer.py
echo "p = subprocess.Popen(arg, shell=True, stdout=subprocess.PIPE)" >> ~/ip_mailer.py
echo "data = p.communicate()" >> ~/ip_mailer.py
echo "split_data = data[0].split()" >> ~/ip_mailer.py
echo "ipaddr = split_data[split_data.index('src') + 1]" >> ~/ip_mailer.py
echo "my_ip = 'Your IP is %s' % ipaddr" >> ~/ip_mailer.py
echo "msg = MIMEText(my_ip)" >> ~/ip_mailer.py
echo "msg['Subject'] = 'IP For RaspberryPi on %s' % today.strftime('%b %d %Y')" >> ~/ip_mailer.py
echo "msg['From'] = gmail_user" >> ~/ip_mailer.py
echo "msg['To'] = to" >> ~/ip_mailer.py
echo "smtpserver.sendmail(gmail_user, [to], msg.as_string())" >> ~/ip_mailer.py
echo "smtpserver.quit()" >> ~/ip_mailer.py
echo "" >> ~/ip_mailer.py


# RUN IP MAILER ON BOOT
sudo sed -i '/printf "My IP address is %s\\n" "$_IP"/ a\
  python /home/pi/ip_mailer.py' /etc/rc.local



echo "Customization completed!  Rebooting Raspberry Pi..."
pause

sudo reboot now
