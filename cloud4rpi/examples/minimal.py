# -*- coding: utf-8 -*-

from time import sleep
import sys
import cloud4rpi


# these functions will be called by device when sending data
def room_temp():
    return 25


def outside_temp():
    return 4


def cpu_temp():
    return 70


def ip_address():
    return '8.8.8.8'


def hostname():
    return 'hostname'


def osname():
    return 'osx'

# Put your device token here. To get the token,
# sign up at https://cloud4rpi.io and create a device.
DEVICE_TOKEN = '__YOUR_DEVICE_TOKEN__'

# Constants
DATA_SENDING_INTERVAL = 30  # secs
DIAG_SENDING_INTERVAL = 60  # secs
POLL_INTERVAL = 0.5  # secs


def main():
    # Put variable declarations here
    variables = {
        'Room Temp': {
            'type': 'numeric',
            'bind': room_temp
        },
        'Outside Temp': {
            'type': 'numeric',
            'bind': outside_temp
        }
    }

    # Put system data declarations here
    diagnostics = {
        'CPU Temp': cpu_temp,
        'IP Address': ip_address,
        'Host Name': hostname,
        'Operating System': osname
    }

    device = cloud4rpi.connect(DEVICE_TOKEN)
    device.declare(variables)
    device.declare_diag(diagnostics)

    device.publish_config()

    # Adds a 1 second delay to ensure device variables are created
    sleep(1)

    try:
        diag_timer = 0
        data_timer = 0
        while True:
            if data_timer <= 0:
                device.publish_data()
                data_timer = DATA_SENDING_INTERVAL

            if diag_timer <= 0:
                device.publish_diag()
                diag_timer = DIAG_SENDING_INTERVAL

            diag_timer -= POLL_INTERVAL
            data_timer -= POLL_INTERVAL
            sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        cloud4rpi.log.info('Keyboard interrupt received. Stopping...')

    except Exception as e:
        error = cloud4rpi.get_error_message(e)
        cloud4rpi.log.error("ERROR! %s %s", error, sys.exc_info()[0])

    finally:
        sys.exit(0)


if __name__ == '__main__':
    main()
