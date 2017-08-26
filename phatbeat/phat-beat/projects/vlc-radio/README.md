## VLC Radio Project

This project rolls a VLC radio onto your Pi, complete with controls via the buttons on pHAT BEAT.

[Check out the full tutorial on our learning portal!](https://learn.pimoroni.com/tutorial/sandyj/internet-radio-on-your-pirate-radio)

**Installing:**

The recommended way to install this project is using our one-line-installer, as this will ensure the pHAT BEAT is properly set up for playback:

```bash
curl https://get.pimoroni.com/vlcradio | bash
```

Alternatively, if you are sure you have a working setup and just want to refresh this project to get all the latest improvements, you can run:

```bash
setup.sh
```

**Using:**

After install you should be asked to reboot. If not, reboot :)

When the VLC Radio is ready to rock, the VU should flash once briefly. Press FF or REV to start playback.

You can also access the VLC server via http on port 8080 if you'd like to add streams or control playback and volume if you are not right next to the radio (leave username blank and use password `raspberry`).

**Playlist:**

A default playlist is supplied with the project, but you can (and probably will want to) tune in your favorite stations, of course.

You can either create a `playlist.m3u` and drop it in your home folder (in `/home/pi/.config/vlc/`), or if you don't feel like logging in via ssh you may also drop the `playlist.m3u` in the `/boot` partition of your SD from another computer and the VLC daemon will copy it in place for your convenience.

Reboot (or restart the `vlcd` service) after editing or creating the file for it to take effect.
