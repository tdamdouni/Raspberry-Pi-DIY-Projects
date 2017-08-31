# Pimoroni-PanTilt-Hat-WebInterface
This is a bootstrap webinterface for the Pimoroni PanTilt Hat

You will need:
* Pimoroni Pan/Tilt HAT Kit
* A Pi Camera
* Streaming URL for

The 15cm ribbon cable supplied with the Pi Camera should be long enough if you're mounting the Pan/Tilt HAT on the Pi. If you're using a Black HAT Hack3r you may need 30cm.

To enable the camera using raspi-config non-interactive mode:

```bash
sudo raspi-config nonint do_camera 0
```

To install the pantilthat library, run:

```bash
curl https://get.pimoroni.com/pantilthat | bash
```
Install the flask modules by running:

```bash
sudo pip install Flask;
sudo pip install Flask-Assets;
sudo pip install Flask-ini
```

Create a config file "config.ini":
```bash
[flask]
debug = true
secret_key = frekelpantilt

[user]
name = admin
pass = pass

[webcam]
url = https://learn.pimoroni.com/static/repos/learn/sandyj/assembling-pan-tilt-at-14.jpg
timeout = 360
```

Finally, to run this example, run:

```bash
./pantiltweb.py.py
```

The servers is running on port 9595. So open the page in your browser (http://127.0.0.1:9595)

# Notes:
1. The buttons have a set of predefined values (for the pan and the tilt).
2. Bootstrap 3 is used
