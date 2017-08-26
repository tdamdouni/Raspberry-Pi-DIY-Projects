# -*- coding: utf-8 -*-

import subprocess


class InvalidTokenError(Exception):
    pass


class MqttConnectionError(Exception):
    def __init__(self, code):
        super(MqttConnectionError, self).__init__()
        self.code = code


class NotSupportedError(Exception):
    pass


__messages = {
    KeyboardInterrupt: 'Interrupted',
    subprocess.CalledProcessError: 'Try run with sudo',
    InvalidTokenError:
        'Device token {0} is invalid. Please verify it.',
}


def get_error_message(e):
    return __messages.get(type(e), 'Unexpected error: {0}').format(e.message)
