#1. Install the necessary software------------------------------
sudo apt-get update
sudo apt-get install hostapd udhcpd -y
sudo apt-get install iptables -y
sudo apt-get install zip unzip -y
sudo apt-get update
#2. Configure DHCP----------------------------------------------
x=tem.tem
touch $x
sudo rm -rf /etc/default/udhcpd
sudo mkdir /etc/default
sudo touch /etc/default/udhcpd
echo "start 192.168.42.2 " >>   $x
echo "end 192.168.42.20" >> $x
echo "interface wlan0" >> $x
echo "remaining yes" >> $x
echo "opt dns 8.8.8.8 4.2.2.2" >> $x
echo "opt subnet 255.255.255.0" >> $x
echo "opt router 192.168.42.1" >> $x
echo "opt lease 864000" >> $x
sudo mv  $x /etc/udhcpd.conf
touch $x
echo  "# Comment the following line to enable" >> $x
echo "#DHCPD_ENABLED=\"no\"" >> $x
echo "# Options to pass to busybox' udhcpd." >> $x
echo "# -S    Log to syslog" >> $x
echo "# -f    run in foreground" >> $x
echo "DHCPD_OPTS=\"-S\"" >> $x
sudo mv $x  /etc/default/udhcpd
	#give the Pi a static IP address 
sudo ifconfig wlan0 192.168.42.1
#------------SETUP Station Interface for Rt5370-------------------------------------
touch $x
sudo cp  /etc/network/interfaces /etc/network/interfaces.bk
echo "source-directory /etc/network/interfaces.d" >> $x
echo "auto lo" >> $x
echo "iface lo inet loopback" >> $x
echo "" >> $x
echo "auto eth0" >> $x
echo "iface eth0 inet dhcp" >> $x
echo "" >> $x
echo "allow-hotplug wlan0" >> $x
echo "iface wlan0 inet dhcp" >> $x
echo "    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf" >> $x
echo "    wireless-power off" >> $x
echo "" >> $x
echo "iface default inet dhcp" >> $x
sudo chown --reference=/etc/network/interfaces $x
sudo chmod --reference==/etc/network/interfaces $x
sudo mv $x /etc/network/interfaces
sudo cp /etc/network/interfaces /etc/network/interfaces.sta 
sudo chmod --reference /etc/network/interfaces.bk /etc/network/interfaces.sta
#------------------------------SETUP AP Interface for Rt5370-------------------------------
touch  $x
echo "source-directory /etc/network/interfaces.d" >> $x
echo "auto lo" >> $x
echo "iface lo inet loopback" >> $x
echo "" >> $x
echo "auto eth0" >> $x
echo "iface eth0 inet dhcp" >> $x
echo "" >> $x
echo "iface wlan0 inet static" >> $x
echo "    address 192.168.42.1" >> $x
echo "    netmask 255.255.255.0" >> $x
echo "    wireless-power off" >> $x
echo "" >> $x
echo "iface default inet dhcp" >> $x
echo "up iptables-restore < /etc/iptables.ipv4.nat" >> $x
sudo chmod --reference==/etc/network/interfaces $x
sudo chown --reference=/etc/network/interfaces $x
sudo mv $x  /etc/network/interfaces.ap
sudo chmod --reference /etc/network/interfaces.bk /etc/network/interfaces.ap
#Config /etc/wpa_supplicant/wpa_supplicant.conf
touch $x
sudo rm -rf /etc/wpa_supplicant/wpa_supplicant.conf
sudo mkdir /etc/wpa_supplicant
sudo touch /etc/wpa_supplicant/wpa_supplicant.conf
echo "ctrl_interface=/var/run/wpa_supplicant" >> $x
echo "update_config=1" >> $x
echo "network={" >> $x
echo "        ssid=\"Robotbase\"" >> $x
echo "        psk=\"Do@nket201234\"" >> $x
echo "}" >> $x
sudo mv $x /etc/wpa_supplicant/wpa_supplicant.conf

#3. Configure HostAPD------------------------------------------------
touch $x
echo "interface=wlan0" >> $x
echo "driver=nl80211" >> $x
echo "ssid=My_AP" >> $x
echo "hw_mode=g" >> $x
echo "channel=6" >> $x
echo "macaddr_acl=0" >> $x
echo "auth_algs=1" >> $x
echo "ignore_broadcast_ssid=0" >> $x
echo  "wpa=2" >> $x
echo "wpa_passphrase=pnptutorials" >> $x
echo "wpa_key_mgmt=WPA-PSK" >> $x
echo "wpa_pairwise=TKIP" >> $x
echo "rsn_pairwise=CCMP" >> $x
sudo mv  $x  /etc/hostapd/hostapd.conf
#4. Configure NAT--------------------------------------------
touch $x
echo "DAEMON_CONF=\"/etc/hostapd/hostapd.conf\"" >> $x
sudo mv $x /etc/default/hostapd

touch $x
sudo sh -c "echo 1 >> /proc/sys/net/ipv4/ip_forward"
sudo echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
sudo sh -c "iptables-save >> /etc/iptables.ipv4.nat"
#------------------------------5. Fire it up! R----------------------------------------
sudo service hostapd start
sudo service udhcpd start
#-----------------------------6.get the hotspot to start on boot----------------------
sudo update-rc.d hostapd enable
sudo update-rc.d udhcpd enable
#------------------------Create wifiConnect.py------------------------------------
sudo apt-get install dnsmasq -y
sudo service dnsmasq start
sudo update-rc.d dnsmasq enable
sudo apt-get install udhcpc -y
sudo cp ap.sh /usr/bin/ap
