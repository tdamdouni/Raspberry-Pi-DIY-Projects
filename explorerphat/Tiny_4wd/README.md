# Tiny_4wd
software for the Coretec Tiny 4wd and setup instructions


Manual control with a game controller like the Rock Candy

1) install the Pimoroni Explorer Python library, instructions can be found on the Explorer page on the Pimoroni website https://shop.pimoroni.com/products/explorer-phat

2) next install the Python 'inputs' library at the command line enter

    sudo pip install inputs
   
3) download TinyPirate.py form here by entering at the command line the following

    wget https://raw.githubusercontent.com/Coretec-Robotics/Tiny_4wd/master/TinyPirate.py
   
4) it's best to restart your Raspberry Pi before running TinyPirate.py

5) after restarting your Pi enter the following to run TinyPirate.py

   sudo python ./TinyPirate.py
   

Manual control with the BlueDot Android app

if you want to install BlueDotPirate.py instead of BlueDotPirateMixed.py replace BlueDotPirateMixed.py with BlueDotPirate.py
   
1) install the Pimoroni Explorer Python library, instructions can be found on the Explorer page on the Pimoroni website https://shop.pimoroni.com/products/explorer-phat

2) follow the instutions on the BlueDot website

   http://bluedot.readthedocs.io/en/latest/gettingstarted.html

3) download BlueDotPirateMixed.py form here by entering at the command line the following

    wget https://raw.githubusercontent.com/Coretec-Robotics/Tiny_4wd/master/BlueDotPirateMixed.py
    
4) it's best to restart your Raspberry Pi before running BlueDotPirateMixed.py

5) after restarting your Pi enter the following to run BlueDotPirateMixed.py

   sudo python3 ./BlueDotPirateMixed.py

