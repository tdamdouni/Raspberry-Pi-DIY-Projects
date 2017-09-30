# Take a pic with raspistill suitable for uploading to Adafruit IO
# https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md
#
# Usage:
#
#   $ ./snap.sh && ./curl.sh
#

# Using the raspistill command with options optimized for filesize. Adapted
# from the answer here:
#
#   https://stackoverflow.com/questions/22675502/raspistill-quality-size-miss-match-file-too-big
#
# - 800x600 resolution
# - roughly 85% jpeg quality
# - no embedded thumbnail
# - no preview window
# - no EXIF data
# - 100ms timeout before taking the photo
# - jpg encoding
# - output filename
raspistill -w 800 -h 600 -q 10 -th none -n -x none -t 100 -e jpg -o sample.jpg
