# Publish a given image to Adafruit IO. Combine with `raspistill` or the
# included ./snap.sh to get a two-script image publishing workflow.
#
# https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md

# get these from your IO account

IO_USERNAME='[redacted]'
IO_KEY='[redacted]'

# take image filename as an argument, default to sample.jpg
IMAGE_PATH=${1:-sample.jpg}

# change this to point at the appropriate feed
FEED_KEY='image-stream'

# publish!
cat $IMAGE_PATH | base64 -w 0 | curl -H "X-AIO-Key: $IO_KEY" -F "value=@-" https://io.adafruit.us/api/v2/$IO_USERNAME/feeds/$FEED_KEY/data

# optional reporting feed, not needed for publishing images
ACTION_FEED_KEY='actions'
BYTES=$(cat sample.jpg | base64 -w 0 | wc -c)
curl -H "X-AIO-Key: $IO_KEY" -F "value=published $BYTES bytes" https://io.adafruit.us/api/v2/$IO_USERNAME/feeds/$ACTION_FEED_KEY/data
