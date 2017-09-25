sudo iptables -t nat -A POSTROUTING -o "$1" -j MASQUERADE
sudo iptables -A FORWARD -i "$1" -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o "$1" -j ACCEPT
