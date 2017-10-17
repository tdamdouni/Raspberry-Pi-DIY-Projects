import paho.mqtt.client as mqtt
import unicornhat as unicorn

import settings


# Define event callbacks
def on_connect(client, userdata, rc):
    if rc == 0:
        print("Connected successfully.")
    else:
        print("Connection failed. rc= " + str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mid " + str(mid) + " received.")


def on_message(client, userdata, msg):
    print("Message received on topic "
          + msg.topic
          + " with QoS "
          + str(msg.qos)
          + " and payload " + msg.payload.decode("utf-8"))

    path = msg.topic.split('/')
    rgb[path[1]] = int(msg.payload.decode("utf-8"))

    for y in range(height):
        for x in range(width):
            if 0 <= y <= 1:
                unicorn.set_pixel(x, y, rgb['red'], 0, 0)
            if 2 <= y <= 3:
                unicorn.set_pixel(x, y, 0, rgb['green'], 0)
            if 4 <= y <= 5:
                unicorn.set_pixel(x, y, 0, 0, rgb['blue'])
            if 6 <= y <= 7:
                unicorn.set_pixel(x, y, rgb['red'], rgb['green'], rgb['blue'])
    unicorn.show()


width, height = 0, 0
rgb = {'red': 0, 'green': 0, 'blue': 0}


def main():
    global width, height
    mqttclient = mqtt.Client()

    # Assign event callbacks
    mqttclient.on_connect = on_connect
    mqttclient.on_subscribe = on_subscribe
    mqttclient.on_message = on_message

    # Connect
    mqttclient.username_pw_set(settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
    mqttclient.connect(settings.MQTT_HOST, int(settings.MQTT_PORT))

    # Start subscription
    mqttclient.subscribe('rgb/+')

    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(0)
    unicorn.brightness(1)
    width, height = unicorn.get_shape()

    mqttclient.loop_forever(timeout=1.0, max_packets=1, retry_first_connection=False)


if __name__ == '__main__':
    main()
