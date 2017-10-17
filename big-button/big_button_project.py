import logging
import time
import random

from pydbus import SystemBus
from gi.repository import GLib

bus = SystemBus()
loop = GLib.MainLoop()

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

import tools
logger = logging.getLogger('BigButton')
# logger.setLevel(logging.WARNING)
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)
logging.debug('Debug message')

logger.addHandler(NullHandler())

# Device address
RED_ADDRESS = 'EB:F6:95:27:84:A0'
YELLOW_ADDRESS = 'E4:43:33:7E:54:1C'
GREEN_ADDRESS = 'FD:6B:11:CD:4A:9B'
BLUE_ADDRESS = 'F7:17:E4:09:C0:C6'
# Button UUIDs
BTN_SRV = 'E95D9882-251D-470A-A062-FA1922DFA9A8'
BTN_A_STATE = 'E95DDA90-251D-470A-A062-FA1922DFA9A8'
# Pin UUIDs
IO_PIN_SRV = 'E95D127B-251D-470A-A062-FA1922DFA9A8'
IO_PIN_DATA = 'E95D8D00-251D-470A-A062-FA1922DFA9A8'
IO_AD_CONFIG = 'E95D5899-251D-470A-A062-FA1922DFA9A8'
IO_PIN_CONFIG = 'E95DB9FE-251D-470A-A062-FA1922DFA9A8'
# LED UUIDs
LED_SRV = 'E95DD91D-251D-470A-A062-FA1922DFA9A8'
LED_TEXT = 'E95D93EE-251D-470A-A062-FA1922DFA9A8'
LED_STATE = 'E95D7B77-251D-470A-A062-FA1922DFA9A8'
LED_SCROLL = 'E95D0D2D-251D-470A-A062-FA1922DFA9A8'
# General Bluez D-Bus Object Paths
#: BlueZ DBus Service Name
BLUEZ_SERVICE_NAME = 'org.bluez'
#: BlueZ DBus adapter interface
ADAPTER_INTERFACE = 'org.bluez.Adapter1'
#: BlueZ DBus device Interface
DEVICE_INTERFACE = 'org.bluez.Device1'

# Bluez GATT D-Bus Object Paths
#: BlueZ DBus GATT manager Interface
GATT_MANAGER_IFACE = 'org.bluez.GattManager1'
#: BlueZ DBus GATT Profile Interface
GATT_PROFILE_IFACE = 'org.bluez.GattProfile1'
#: BlueZ DBus GATT Service Interface
GATT_SERVICE_IFACE = 'org.bluez.GattService1'
#: BlueZ DBus GATT Characteristic Interface
GATT_CHRC_IFACE = 'org.bluez.GattCharacteristic1'
#: BlueZ DBus GATT Descriptor Interface
GATT_DESC_IFACE = 'org.bluez.GattDescriptor1'


class ButtonBox:
    def __init__(self, dev_address, btn_callback):
        self.address = dev_address
        self.btn_callbacks = btn_callback

        self.dev_obj = bus.get(BLUEZ_SERVICE_NAME,
                               tools.get_dbus_path(self.address))
        self.dev_btn = None
        self.dev_pins = None
        self.dev_text = None
        self.dev_leds = None
        self.dev_scrll_spd = None

        self.dev_obj.onPropertiesChanged = self.dev_connect
        self.dev_obj.Connect()

    def dev_connect(self, *args):
        if 'ServicesResolved' in args[1]:
            if args[1]['ServicesResolved']:
                self.get_gatt_details()

    def dev_disconnect(self):
        self.dev_obj.Disconnect()

    def get_gatt_details(self):
        self.dev_btn_gatt()
        self.dev_pin_gatt()
        self.dev_led_gatt()

    def dev_btn_gatt(self):
        self.dev_btn = bus.get(BLUEZ_SERVICE_NAME,
                               tools.get_dbus_path(self.address, BTN_SRV, BTN_A_STATE))
        self.dev_btn.StartNotify()
        self.dev_btn.onPropertiesChanged = self.btn_pressed

    def dev_pin_gatt(self):
        dev_ad_config = bus.get(BLUEZ_SERVICE_NAME,
                                tools.get_dbus_path(self.address, IO_PIN_SRV, IO_AD_CONFIG))
        dev_io_config = bus.get(BLUEZ_SERVICE_NAME,
                                tools.get_dbus_path(self.address, IO_PIN_SRV, IO_PIN_CONFIG))
        self.dev_pins = bus.get(BLUEZ_SERVICE_NAME,
                                tools.get_dbus_path(self.address, IO_PIN_SRV, IO_PIN_DATA))
        dev_ad_config.WriteValue([0x00, 0x00, 0x00, 0x00], {})
        dev_io_config.WriteValue([0x00, 0x00, 0x00, 0x00], {})
        self.dev_pins.WriteValue([0x08, 0x00, 0x0C, 0x00], {})

    def dev_led_gatt(self):
        self.dev_text = bus.get(BLUEZ_SERVICE_NAME,
                                tools.get_dbus_path(self.address, LED_SRV, LED_TEXT))
        self.dev_leds = bus.get(BLUEZ_SERVICE_NAME,
                                tools.get_dbus_path(self.address, LED_SRV, LED_STATE))
        self.dev_scrll_spd = bus.get(BLUEZ_SERVICE_NAME,
                                     tools.get_dbus_path(self.address, LED_SRV, LED_SCROLL))

    def btn_light_on(self):
        logger.debug('{} on'.format(self.address))
        self.dev_pins.WriteValue([0x08, 0x00, 0x0C, 0x01], {})

    def btn_light_off(self):
        logger.debug('{} off'.format(self.address))
        self.dev_pins.WriteValue([0x08, 0x00, 0x0C, 0x00], {})

    def btn_pressed(self, *args):
        logger.info('Button {} Pressed: {}'.format(self.address, args))
        if 'Value' in args[1]:
            if args[1]['Value'][0] > 0:
                self.btn_callbacks(self.address)


class ButtonGame:
    def __init__(self):
        self.score = 0
        self.btn_active = None
        self.game_length = 20  # In seconds
        self.game_start_time = None
        self.game_active = False
        self.red = ButtonBox(RED_ADDRESS, self.button_press_event)
        self.yellow = ButtonBox(YELLOW_ADDRESS, self.button_press_event)
        self.green = ButtonBox(GREEN_ADDRESS, self.button_press_event)
        self.blue = ButtonBox(BLUE_ADDRESS, self.button_press_event)
        self.btn_list = {RED_ADDRESS: ['red', self.red],
                         YELLOW_ADDRESS: ['yellow', self.yellow],
                         GREEN_ADDRESS: ['green', self.green],
                         BLUE_ADDRESS: ['blue', self.blue]}

    def update_score(self):
        if self.game_active:
            self.score += 1

    def reset_score(self):
        if not self.game_active:
            self.score = 0

    def game_over(self):
        self.game_active = False
        self.btn_active = None
        self.set_active(None)
        logger.info('Game Ended!  Score: {}'.format(self.score))

    def set_active(self, btn_id):
        for btn in [item[1] for item in self.btn_list.values()]:
            btn.btn_light_off()
        if btn_id is not None:
            self.btn_active = self.btn_list[btn_id][0]
            self.btn_list[btn_id][1].btn_light_on()

    def button_press_event(self, btn_address):
        if int(time.time()) - self.game_start_time > self.game_length:
            logger.debug('Game Over')
            self.game_over()
        elif self.correct_btn(self.btn_list[btn_address][0]):
            logger.debug('Correct button pressed')
            self.update_score()
            self.next_btn()
        else:
            logger.debug('Wrong button pressed')

    def correct_btn(self, btn_id):
        logger.debug('Check pressed {} against {}'.format(btn_id, self.btn_active))
        if btn_id == self.btn_active and self.game_active:
            return True
        else:
            return False

    def next_btn(self):
        self.set_active(random.choice(list(self.btn_list.keys())))
        logger.debug('Next button chosen: {}'.format(self.btn_active))

    def game_start(self):
        logger.debug('Game start!!')
        self.reset_score()
        self.game_start_time = int(time.time())
        self.game_active = True
        self.next_btn()

    def game_exit(self):
        for btn in [item[1] for item in self.btn_list.values()]:
            btn.btn_light_off()
            btn.dev_obj.Disconnect()
