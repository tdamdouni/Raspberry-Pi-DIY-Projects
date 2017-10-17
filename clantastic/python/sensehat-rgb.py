import time

from sense_emu import SenseHat
import paho.mqtt.client as mqtt

import settings

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)


def range_calculator(input_value, input_min, input_max, output_min=0, output_max=255):
    # http://stackoverflow.com/a/929107/1049688
    return int((((input_value - input_min) * (output_max - output_min)) / (input_max - input_min)) + output_min)


def on_publish(client, userdata, mid):
    print("Message " + str(mid) + " published.")


def main():
    mqttclient = mqtt.Client()
    mqttclient.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
    mqttclient.connect(settings.MQTT_HOST, int(settings.MQTT_PORT))
    mqttclient.on_publish = on_publish

    while True:
        temp = sense.temp
        pressure = sense.pressure
        humidity = sense.humidity
        print('The temperature is {}, the pressure is {}, and the humidity is {}'.format(temp, pressure, humidity))

        red = range_calculator(temp, -30, 105)
        green = range_calculator(pressure, 260, 1260)
        blue = range_calculator(humidity, 0, 100)
        print("Red's value is {}, green's value is {}, and blue's value is {}".format(red, green, blue))

        mqttclient.publish('rgb/red', red, retain=True)
        mqttclient.publish('rgb/green', green, retain=True)
        mqttclient.publish('rgb/blue', blue, retain=True)
        time.sleep(0.3)


if __name__ == '__main__':
    main()
