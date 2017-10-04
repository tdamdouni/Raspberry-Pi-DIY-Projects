# pi-shut
******************************************
**Pi Shutdown Service for Headless Units**  
******************************************
Safe shutdown and start pi boards using a mommentary push buton  
1. Run the installer.
```
sudo chmod +x /home/pi/pi-shut/installer.sh  
sudo /home/pi/pi-shut/installer.sh  
```
2. Wire the pi as per diagram.  
3. Start the shutdown service.  
```
sudo systemctl start on-off-pushbutton.service
```
