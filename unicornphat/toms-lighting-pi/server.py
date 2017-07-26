import time
import unicornhat as unicorn

from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def color():
    hex_color = request.args.get('color')

    red, green, blue = map(ord, hex_color.decode('hex'))

    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(1)
    width, height = unicorn.get_shape()

    for y in range(height):
        for x in range(width):
            unicorn.set_pixel(x, y, red, green, blue)
            unicorn.show()
            time.sleep(0.03)

    return "Success, set to " + hex_color


@app.route("/off")
def off():
    unicorn.off()
    unicorn.show()

    return "Success, turned off"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
