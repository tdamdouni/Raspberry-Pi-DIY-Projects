from picamera import PiCamera
from picamera.array import PiRGBArray
from sense_hat import SenseHat

sense = SenseHat()

while True:
    with PiCamera() as camera:
        camera.resolution = (64, 64)
        with PiRGBArray(camera, size=(8, 8)) as stream:
            camera.capture(stream, format='rgb', resize=(8, 8))
            image = stream.array

    pixels = [
        pixel
        for row in image
        for pixel in row
    ]

    sense.set_pixels(pixels)
