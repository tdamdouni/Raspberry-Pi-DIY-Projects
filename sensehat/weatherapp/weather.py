from flask import Flask, render_template
from sense_hat import SenseHat

app = Flask(__name__)

@app.route('/')

def index():
    sense = SenseHat()

    celcius = round(sense.get_temperature(), 1)
    #fahrenheit = round(1.8 * celcius + 32, 1)
    humidity = round(sense.get_humidity(), 1)
    pressure = round(sense.get_pressure(), 1)

    #return render_template('weather.html', celcius=celcius, fahrenheit=fahrenheit)
    return render_template('weather.html', celcius=celcius, humidity=humidity, pressure=pressure)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
