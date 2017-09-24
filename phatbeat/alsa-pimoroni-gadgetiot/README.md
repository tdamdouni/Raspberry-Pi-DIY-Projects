# Pulse Audio Configuration for Raspberry Pi Audio Systems

This Pulse Audio configuration is designed to sit between your audio source and sink, to keep the audio device open and mitigate speaker pops.

This is only for I2S DAC devices on the Raspberry Pi that pop when they are started/stopped.

## Installing

First, install `pulseaudio` if it's not already installed:

```
sudo apt update
sudo apt install pulseaudio
```

#### /etc/pulse/client.conf

Edit `/etc/pulse/client.conf` and add or change these lines (anything preceeded with "`;`" is commented out so be sure to remove it):

You can edit a file with `sudo nano /etc/pulse/client.conf` and find lines by pressing Ctrl+W, typing your search term and hitting enter.

```
autospawn = no
default-server = unix:/tmp/pulseaudio.socket
```

#### /etc/pulse/default.pa

Edit `/etc/pulse/default.pa` and find the line `load-module module-suspend-on-idle`, add ` timeout=604800` onto the end.

It should look like this:

```
### Automatically suspend sinks/sources that become idle for too long
load-module module-suspend-on-idle timeout=604800
```

Next, find the line `load-module module-native-protocol-tcp` and add ` auth-ip-acl=127.0.0.1` to the end.

It should look like this:

```
### Allow local connections over tcp, for mopidy etc
load-module module-native-protocol-tcp auth-ip-acl=127.0.0.1
```

Then, find the line `load-module module-native-protocol-unix` and add ` auth-anonymous=1 socket=/tmp/pulseaudio.socket`.

It should look like this:

```
### Allow unauthenticated connections from other users so aplay, etc work via pulse
load-module module-native-protocol-unix auth-anonymous=1 socket=/tmp/pulseaudio.socket
```

##### If you want to use a VU Meter

If you're using Pi VU Meter with pHAT BEAT, Speaker pHAT or other compatible board then find the line that starts `### Automatically load driver modules` and add the following before it:

```
load-module module-alsa-sink device=pivumeter
```

This will make sure Pulse outputs through the VU Meter plugin, rather than right to the audio device.

#### /etc/systemd/system/pulseaudio.service

Finally the `pulseaudio.service` file:

```
[Unit]
Description=PulseAudio Daemon
After=sound.target
Requires=sound.target

[Install]
WantedBy=default.target

[Service]
Restart=always
Type=simple
PrivateTmp=false
ExecStart=/usr/bin/pulseaudio --realtime --disallow-exit --no-cpu-limit --log-target=syslog
ExecStop=/usr/bin/pulseaudio --kill
```

Should go into `/etc/systemd/system/pulseaudio.service` and be enabled with:

```
sudo systemctl daemon-reload
sudo systemctl enable pulseaudio
sudo systemctl start pulseaudio
```

## Verifying

Check that pulse is running by entering:

```
sudo systemctl status pulseaudio
```

This will also show you any relevant log output.

## Tips & Tricks

#### Fix Choppy Audio When Streaming

One possible fix for this problem- particularly with Shairport Sync -is to disable WiFi power management. 

You can test this by running `sudo iw wlan0 set power_save off` and, if it works, make it permenant by editing `/etc/network/interfaces` and:

```
allow-hotplug wlan0
iface wlan0 inet manual
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
    wireless-power off # <---- Adding this line
```

## Troubleshooting

First, double check that you followed all the config steps above correctly.

A useful troubleshooting tool is `aplay`, you can usee `aplay -L` to show a list of device names, including pulseaudio if it's running.

#### No sound when running pulseaudio

Try restarting your audio applications, and ensure they're outputting audio via pulse. This pulse configuration will tie up the raw sound device (by necessity to keep the clock running) and all sound must go via the daemon.

Check `aplay --list-devices`, if you have more than one device listed here your audio might be playing to the other one, or pulse might have selected the wrong device as its sink.