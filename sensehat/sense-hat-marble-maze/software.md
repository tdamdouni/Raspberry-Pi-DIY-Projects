# Software installation

Connect your Sense HAT and boot up the Raspberry Pi.

First update and upgrade your system by entering the following commands into a terminal window (while connected to the internet):

```bash
sudo apt-get update
sudo apt-get upgrade
```

Now install the Sense HAT software packages:

```bash
sudo apt-get install sense-hat
sudo pip-3.2 install pillow
```

Finally, reboot the Pi to complete the installation:

```bash
sudo reboot
```
