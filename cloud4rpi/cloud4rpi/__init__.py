# -*- coding: utf-8 -*-

import time
import logging
from logging import StreamHandler, Formatter
from logging.handlers import RotatingFileHandler


from cloud4rpi.config import mqqtBrokerHost
from cloud4rpi.config import mqttBrokerPort
from cloud4rpi.config import loggerName

from cloud4rpi.device import Device
from cloud4rpi.mqtt_api import MqttApi
from cloud4rpi.errors import get_error_message

log = logging.getLogger(loggerName)
log.setLevel(logging.INFO)
log.addHandler(StreamHandler())


def connect(device_token,
            host=mqqtBrokerHost,
            port=mqttBrokerPort):
    api = MqttApi(device_token, host, port)
    __attempt_to_connect_with_retries(api)
    return Device(api)


def __attempt_to_connect_with_retries(api, attempts=10):
    retry_interval = 5
    for attempt in range(attempts):
        try:
            api.connect()
        except Exception as e:
            log.debug('MQTT connection error %s. Attempt %s', e, attempt)
            time.sleep(retry_interval)
            continue
        else:
            break
    else:

        raise Exception('Impossible to connect to MQTT broker. Quiting.')


def set_logging_to_file(log_file_path):
    log_file = RotatingFileHandler(
        log_file_path,
        maxBytes=1024 * 1024,
        backupCount=10
    )
    log_file.setFormatter(Formatter('%(asctime)s: %(message)s'))
    log.addHandler(log_file)
