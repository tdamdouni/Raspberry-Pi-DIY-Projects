# Smartphone-Doorlock
Doorlock that can be locked or unlocked through your smartphone

You’ll want to make sure you have [node.js](https://nodejs.org/en/) installed on your Raspberry Pi. Adafruit has a nice guide on their [website](https://learn.adafruit.com/node-embedded-development/installing-node-dot-js).

## Installation
Navigate to the folder you want to clone the repository and type

```
git clone https://github.com/HackerHouseYT/Smartphone-Doorlock.git
```

Once done cloning, navigate into the folder.

```
cd Smartphone-Doorlock
```

Install the dependencies

```
sudo npm install
```

Add the Blynk auth token by opening up the `doorlock.js` file and replacing the `blynkToken` variable.

```
vim doorlock.js
```

Scroll down, press `i` to edit in vim, and replace the token between the single quotes. Press `esc` then type `:wq` to save and quit.

`sudo node doorlock.js` starts the program.

## Running at Startup

To run at startup, you can add the start command to your `rc.local`.

Type `pwd` to get your current directory. I highlighted this and copied it with `control-c`.

Edit the `rc.local` file with vim.

```
sudo vim /etc/rc.local
```

Press `i`, then scroll down and add `sudo node <Your Directory From pwd>/doorlock.js`

Press `esc`, then type `:wq!` to save and exit. Restart the Pi to start the program.

