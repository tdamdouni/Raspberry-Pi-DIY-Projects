Mini Pan-Tilt Face Tracker
==========================

You will need:
* Pimoroni Pan/Tilt HAT Kit
* A Pi Camera

The 15cm ribbon cable supplied with the Pi Camera should be long enough if you're mounting the Pan/Tilt HAT on the Pi. If you're using a Black HAT Hack3r you may need 30cm.

To enable the camera using raspi-config non-interactive mode:

```bash
sudo raspi-config nonint do_camera 0
```

You will also need to make sure your Pi is up-to-date and install OpenCV for Python:

```bash
sudo apt-get install python-opencv python3-opencv opencv-data
```

To install the pantilthat library, run:

```bash
curl https://get.pimoroni.com/pantilthat | bash
```

Finally, to run this example, run:

```bash
./facetracker_lbp.py
```

Note
----

You can use an Arduino to drive the servos, or drive them directly off your Pi, but I found PanTilt HAT to be the most stable, reliable and satisfying method and thus this code is written with it in mind.
