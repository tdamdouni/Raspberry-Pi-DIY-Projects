https://gist.github.com/Gadgetoid/47d8f873fde39fcbe83e6dab0e855f72

Starting from Jessie or Jessie Lite

```
curl get.pimoroni.com/phatbeat | bash
```

Then install VLC:

```
sudo apt-get install vlc-nox
```

Create a new dir `vlc` in `/home/pi` and copy all of the below files into it.

Then run `crontab -e` and add:

```
@reboot /home/pi/vlc/start.sh
```