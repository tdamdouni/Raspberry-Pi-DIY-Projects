#! /bin/bash
if [ -z "$1" ] 
then
  echo "No Input Name, select default name:ThanhLe_handsome"
  name="ThanhLe_handsome"
  sudo sed -i -e "s/\(ssid=\).*/\1$name/" /etc/hostapd/hostapd.conf
  
else
  sudo sed -i -e "s/\(ssid=\).*/\1$1/" /etc/hostapd/hostapd.conf
fi
if [ -z  "$2" ] 
then
  echo "No Pass Hotspot"
  x=0
  sudo sed -i -e "s/\(wpa=\).*/\1$x/" /etc/hostapd/hostapd.conf
else
  x=2
  sudo sed -i -e "s/\(wpa=\).*/\1$x/" /etc/hostapd/hostapd.conf
  sudo sed -i -e "s/\(wpa_passphrase=\).*/\1$2/" /etc/hostapd/hostapd.conf
fi
dd="0"
sudo sed -i -e "s/\(ignore_broadcast_ssid=\).*/\1$dd/" /etc/hostapd/hostapd.conf
sudo /etc/init.d/hostapd stop
sudo /etc/init.d/udhcpd stop
sudo /etc/init.d/dnsmasq stop
sudo ifdown wlan0
sudo ifconfig wlan0 down
sudo rm -rf /etc/network/interfaces
sudo cp /etc/network/interfaces.ap /etc/network/interfaces
sudo ifconfig wlan0 up
sudo ifup wlan0
sudo /etc/init.d/hostapd restart
sudo /etc/init.d/udhcpd restart
sudo /etc/init.d/dnsmasq restart
sudo service hostapd status
sudo service udhcpd status
sudo service dnsmasq status
