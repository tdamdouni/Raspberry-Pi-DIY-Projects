### Additional notes

Original blog post - http://blog.alexellis.io/live-stream-with-docker/

**How do I rebuild the image from scratch?**

This will take several hours on a Raspberry Pi Zero - but less time on a Pi 2 or Pi 3. You can edit the Dockerfile for a Pi 2/3 and change `RUN make` to `RUN make -j 4` to take advantage of the quad-core processor.

```
$ git clone https://github.com/alexellis/raspberrypi-youtube-streaming/
$ cd streaming
$ docker build -t alexellis2/streaming .
```

**How do I edit the settings?**

You should edit the `entry.sh` file and then write a new Dockerfile using my image as a base:

Place a `Dockerfile` in a new directory with this contents:

```
FROM alexellis2/streaming:17-5-2017
COPY entry.sh entry.sh
```

Then run a Docker build - this should take less than 10 seconds since we're only adding on top of the existing image.

```
$ cd streaming
$ docker build -t alexellis2/streaming .
```

**How can I enter bash on the container?**

You can replace the start-up command (`ENTRYPOINT`) like this:

```
$ docker run --entrypoint=/bin/bash --privileged --name cam -ti alexellis2/streaming:17-5-2017
```
