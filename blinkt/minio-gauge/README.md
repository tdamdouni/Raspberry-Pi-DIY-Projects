# minio-gauge
A Minio pressure gauge with the Raspberry Pi and Blinkt! from Pimoroni, see in real-time how busy your S3 cloud storage is.

You can run Minio on the cloud, on premesis or even on a Raspberry Pi, just configure the webhooks to fire into the Raspberry Pi. That way it can track the activity in Redis (low latency) and then display the colours as things ramp up.

This project runs under Docker and has three components:

* Redis queue
* Webhook listener (accepts HTTP POSTs on port 3000 and increments a key)
* LED updater (sets the Blinkt! colours depending on the threshold)

The pressure display is set to ease off after 2 seconds and goes - green, red, blue.

Checkout the video demo here:

> [Video demo](https://www.youtube.com/watch?v=7lXg3jJs0bU)

### Get ready

Install Docker, pip and Docker-compose

```
# curl -sSL get.docker.com
# apt-get install python-pip
# pip install docker-compose
```

### Get set

```
# docker-compose build
```

This step could take a while, especially on the Pi Zero.

### Go!

```
# docker-compose up -d
```

* Now start the code and find your Raspberry Pi's IP address.
* Edit `~/.minio/config.json` and set your webhook endpoint to the address, i.e. http://raspberrypi.local:3000/
