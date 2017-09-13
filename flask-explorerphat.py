# http://forums.pimoroni.com/t/explorer-hat-pro-flickering-light-when-i-turn-it-on-using-flask-endpoint/5910/3

from flask import Flask
from flask import make_response
import explorerhat as eh

app = Flask(__name__)

@app.route("/")
@app.route("/on/<light>")
def turnon(light = 'None'):
        if light == 'yellow':
                eh.light.yellow.on()
        return make_response(light + ' is on')
@app.route("/off/<light>")
def turnoff(light = 'None'):
        if light == 'yellow':
                eh.light.yellow.off()
        return light + ' is off'

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80, debug = True)