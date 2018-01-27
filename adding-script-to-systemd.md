_https://forums.pimoroni.com/t/unicorn-hat-python-script-stops-after-8-hours/6275/12_

Although probably what you really want is a systemd unit to start up your Python script. Something like:

```
[Unit]
Description=My Python Service
After=multiuser.target
Requires=local-fs.target

[Service]
Restart=always
Type=simple
ExecStart=/usr/bin/python /home/pi/Pimoroni/unicornhathd/examples/candle.py

[Install]
WantedBy=default.target
```

Save this as a file by running: `sudo nano /etc/systemd/system/mypython.service` and pasting in the above.

Then reload systemd:

`sudo systemctl daemon-reload`

And start your new service:

`sudo systemctl start mypython`

You can also get its status:

`sudo systemctl status mypython`

And stop it:

`sudo systemctl stop mypython`

And enable it to auto-start on boot:

`sudo systemctl enable mypython`