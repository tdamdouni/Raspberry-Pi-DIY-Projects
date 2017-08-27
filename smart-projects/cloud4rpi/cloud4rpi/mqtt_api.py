# -*- coding: utf-8 -*-

import time
import logging
import json
from math import floor

from cloud4rpi import config
from cloud4rpi import utils
from cloud4rpi.errors import MqttConnectionError

import paho.mqtt.client as mqtt

KEEP_ALIVE_INTERVAL = 30
MQTT_ERR_SUCCESS = 0
CONNECT_RESULT_UNDEFINED = 255

log = logging.getLogger(config.loggerName)


class MqttApi(object):
    def __init__(self,
                 device_token,
                 host=config.mqqtBrokerHost,
                 port=config.mqttBrokerPort):
        utils.guard_against_invalid_token(device_token)

        def noop_on_command(cmd):
            pass

        self.__device_token = device_token
        self.__client = mqtt.Client(device_token, clean_session=False)
        self.__host = host
        self.__port = port
        self.__connect_result = None

        self.on_command = noop_on_command

    def __format_topic(self, tail):
        return 'devices/{0}/{1}'.format(self.__device_token, tail)

    def connect(self):
        def on_connect(client, userdata, flags, rc):
            self.__connect_result = rc
            if rc != MQTT_ERR_SUCCESS:
                log.error('Connection failed: %s', rc)
                raise MqttConnectionError(rc)
            topic = self.__format_topic('commands')
            log.debug('Listen for %s', topic)
            self.__client.subscribe(topic, qos=1)

        def on_message(client, userdata, msg):
            log.info('Command received %s: %s', msg.topic, msg.payload)
            if callable(self.on_command):
                payload = msg.payload.decode() \
                    if isinstance(msg.payload, bytes) else msg.payload
                self.on_command(json.loads(payload))

        def on_disconnect(client, userdata, rc):
            log.info('MQTT disconnected with code: %s', rc)
            self.__on_disconnect(rc)

        self.__client.on_connect = on_connect
        self.__client.on_message = on_message
        self.__client.on_disconnect = on_disconnect

        log.info('MQTT connecting %s:%s', self.__host, self.__port)
        self.__client.connect(self.__host, self.__port,
                              keepalive=KEEP_ALIVE_INTERVAL)

        self.__connect_result = CONNECT_RESULT_UNDEFINED
        self.__client.loop_start()

        while self.__connect_result == CONNECT_RESULT_UNDEFINED:
            time.sleep(.01)

    def __on_disconnect(self, rc):
        if rc == MQTT_ERR_SUCCESS:
            return

        attempts = 0
        retry_interval = 0.5
        while True:
            attempts += 1
            log.info('Attempt #%s to reconnect after %s sec', attempts,
                     floor(retry_interval))
            retry_interval = min(retry_interval * 2, 100)
            try:
                self.__client.reconnect()
                log.info("Reconnected!")
                return
            except Exception as e:
                log.info('Reconnection failed: %s', str(e))
                time.sleep(retry_interval)

    def disconnect(self):
        self.__client.loop_stop()
        self.__client.disconnect()

    def publish_config(self, cfg):
        self.__publish(self.__format_topic('config'), cfg)

    def publish_data(self, data):
        self.__publish(self.__format_topic('data'), data)

    def publish_diag(self, diag):
        self.__publish(self.__format_topic('diagnostics'), diag)

    def __publish(self, topic, payload=None):
        if payload is None:
            return
        msg = {
            'ts': utils.utcnow(),
            'payload': payload,
        }
        log.info('Publishing %s: %s', topic, msg)
        self.__client.publish(topic, payload=json.dumps(msg))
