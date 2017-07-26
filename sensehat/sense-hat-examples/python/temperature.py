from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)

while True:
    temp = sense.temp
    print(temp)

    pixels = [red if i < temp else blue for i in range(64)]

    sense.set_pixels(pixels)
