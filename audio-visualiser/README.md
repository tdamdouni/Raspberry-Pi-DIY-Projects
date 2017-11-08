# audio-visualiser
Code for a Raspberry Pi audio-visualiser.

Required packages:

```
    python-alsaaudio
    mpg123
	unicornhat
```

To install the Unicorn HAT:

```bash
curl -sS get.pimoroni.com/unicornhat | bash
```

To force HDMI audio:

1. sudo nano /boot/config.txt

2. Add the following:

```
    hdmi_force_hotplug=1
    hdmi_force_edid_audio=1
```

To convert a mp3 file to a wav file:

```bash
    mpg123 -w 'output.wav' 'input.mp3'
```

To run the script:

```bash
    sudo python visualiser.py output.wav
```