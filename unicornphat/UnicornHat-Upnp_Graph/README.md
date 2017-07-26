# UnicornHat-Upnp_Graph
Visualize your Routers bandwidth usage with a raspberry pi and a unicorn hat (or pHat).

Included are two different scripts:
- Vertical: Bars
- Horizontal: Graph

See a early version in action:
https://plus.google.com/+MartinHauck/posts/fMtZ8hDCtmN

Get the unicorn hat here: 
https://shop.pimoroni.com/products/unicorn-hat
https://shop.pimoroni.com/products/unicorn-phat

Install:
install git "sudo apt-get install git"
clone this repo "git clone https://github.com/magicmad/UnicornHat-Upnp_Graph.git"
make connection rate script executable: "chmod +x connection_rate.sh"
adjust the maximum bandwidth values to your internet connection in tm_bar.py and tm_graph.py

Run:
"sudo python3 tm_bar.py"

Setup autostart:
add the following lines to /etc/rc.local above "exit 0"
 #run tm_bar
 python3 /home/pi/UnicornHat-Upnp_Graph/tm_bar.py

Background:
It uses UPNP queries to get the current bandwidth usage from the router.
So far, this has been tested with a AVM fritzbox only. 
It could be improved to query those values from python with soap.
