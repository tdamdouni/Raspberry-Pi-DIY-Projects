# -*- coding: utf-8 -*-
# These tests need a running mqtt broker instance

import os
import json
import unittest
from threading import Event
from cloud4rpi import MqttApi
from cloud4rpi.errors import InvalidTokenError

import paho.mqtt.client as mqtt


class MqttMessageProbe(object):
    def __init__(self, on_message):
        self.__client = mqtt.Client()
        self.__on_message = on_message
        self.__client.connect('localhost')
        self.last_message = None

        def on_msg(client, userdata, message):
            self.last_message = message
            on_message()

        self.__client.on_message = on_msg
        self.__client.subscribe('iot-hub/messages/#')
        self.__client.loop_start()

    def dispose(self):
        self.__client.loop_stop()
        self.__client.disconnect()


class MqttCommandPublisher(object):
    def __init__(self):
        self.__client = mqtt.Client()
        self.__client.connect('localhost')
        self.__client.loop_start()

    def dispose(self):
        self.__client.loop_stop()
        self.__client.disconnect()

    def publish_command(self, device_token, command):
        self.__client.publish('iot-hub/commands/{0}'.format(device_token),
                              payload=json.dumps(command))


class _TimeoutError(Exception):  # avoid from pylint redefined-builtin
    pass


class AsyncTestCase(unittest.TestCase):
    def setUp(self):
        super(AsyncTestCase, self).setUp()
        self._done = Event()
        self._done.clear()

    def tearDown(self):
        super(AsyncTestCase, self).tearDown()
        self._done.clear()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = get_async_test_timeout()

        self._done.wait(timeout)

        if not self.is_done():
            raise _TimeoutError()

    def stop(self):
        self._done.set()

    def is_done(self):
        return self._done.isSet()


def get_async_test_timeout(default=5):
    try:
        return float(os.environ.get('ASYNC_TEST_TIMEOUT'))
    except (ValueError, TypeError):
        return default


@unittest.skip("The Real mqtt broker required")
class TestMqttApi(AsyncTestCase):
    def setUp(self):
        super(TestMqttApi, self).setUp()
        self.test_probe = MqttMessageProbe(on_message=self.stop)

    def tearDown(self):
        super(TestMqttApi, self).tearDown()
        self.test_probe.dispose()

    @staticmethod
    def create_api_client():
        client = MqttApi('4GPZFMVuacadesU21dBw47zJi', host='localhost')
        client.connect()
        return client

    def testCtorThrowsOnInvalidToken(self):
        with self.assertRaises(InvalidTokenError):
            MqttApi('invalid device token')

    def testPublishConfig(self):
        client = self.create_api_client()

        variables = [
            {'name': 'Temperature', 'type': 'numeric'},
            {'name': 'Cooler', 'type': 'bool'},
            {'name': 'TheAnswer', 'type': 'numeric'},
        ]
        client.publish_config(variables)

        self.wait()

        actual_msg = self.test_probe.last_message
        self.assertEqual('iot-hub/messages/4GPZFMVuacadesU21dBw47zJi',
                         actual_msg.topic)
        self.assertEqual('config', json.loads(actual_msg.payload)['type'])
        self.assertEqual(variables, json.loads(actual_msg.payload)['payload'])

    def testPublishData(self):
        client = self.create_api_client()

        data = {
            'Temperature': 36.6,
            'Cooler': True,
            'TheAnswer': 42
        }
        client.publish_data(data)

        self.wait()

        actual_msg = self.test_probe.last_message
        self.assertEqual('iot-hub/messages/4GPZFMVuacadesU21dBw47zJi',
                         actual_msg.topic)
        self.assertEqual('data', json.loads(actual_msg.payload)['type'])
        self.assertEqual(data, json.loads(actual_msg.payload)['payload'])

    def testPublishDiag(self):
        client = self.create_api_client()

        diag = {
            'IPAddress': '127.0.0.1',
            'Hostname': 'weather_station',
            'CPU Load': 99
        }
        client.publish_diag(diag)

        self.wait()

        actual_msg = self.test_probe.last_message
        self.assertEqual('iot-hub/messages/4GPZFMVuacadesU21dBw47zJi',
                         actual_msg.topic)
        self.assertEqual('system', json.loads(actual_msg.payload)['type'])
        self.assertEqual(diag, json.loads(actual_msg.payload)['payload'])

    def testOnCommand(self):
        def on_command(command):
            self.assertEqual({'Cooler': True}, command)
            self.stop()

        client = self.create_api_client()
        client.on_command = on_command

        commander = MqttCommandPublisher()
        commander.publish_command(
            '4GPZFMVuacadesU21dBw47zJi',
            {'Cooler': True}
        )

        self.wait()
