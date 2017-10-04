from time import sleep

from mote import Mote
from bluezero import constants
from bluezero import tools
from bluezero import adapter
from bluezero import device
from bluezero.GATT import Characteristic

display_on = False
lights = Mote()

mote_pixels = 16
lights.configure_channel(1, mote_pixels, False)


def on_accel_change(iface, changed_props, invalidated_props):
    print('Accel!')
    global display_on
    if iface != constants.GATT_CHRC_IFACE:
        return

    if not len(changed_props):
        return

    accel_val = changed_props.get('Value', None)
    if not accel_val:
        return

    # Read button value
    x = abs(int.from_bytes(accel_val[0:1], byteorder='little', signed=True))
    y = abs(int.from_bytes(accel_val[2:3], byteorder='little', signed=True))
    z = abs(int.from_bytes(accel_val[4:5], byteorder='little', signed=True))

    print(x, y, z)
    for pixel in range(mote_pixels):
        lights.set_pixel(1, pixel, x, y, z)
    if display_on:
        lights.show()


def on_button_b(iface, changed_props, invalidated_props):
    global display_on
    print('Button B pressed!')
    if iface != constants.GATT_CHRC_IFACE:
        return

    if not len(changed_props):
        return

    value = changed_props.get('Value', None)
    if not value:
        return

    value = int.from_bytes(value, byteorder='little', signed=False)

    if value > 0:
        global display_on
        print('On')
        lights.clear()
        for pixel in range(mote_pixels):
            print('Set pixel ', pixel)
            lights.set_pixel(1, pixel, 125, 125, 125)
            sleep(0.1)
            lights.show()
        display_on = True


def on_button_a(iface, changed_props, invalidated_props):
    print('Button A pressed!')
    if iface != constants.GATT_CHRC_IFACE:
        return

    if not len(changed_props):
        return

    value = changed_props.get('Value', None)
    if not value:
        return

    value = int.from_bytes(value, byteorder='little', signed=False)

    if value > 0:
        global display_on
        display_on = False
        print('Off')
        lights.clear()
        lights.show()

print('power adapter')
dongle = adapter.Adapter('/org/bluez/hci0')
if not dongle.powered():
    dongle.powered(True)
print('discovery')
dongle.nearby_discovery()
ubit = device.Device(tools.device_dbus_path(constants.DEVICE_INTERFACE,
                                            'puteg')[0])
while True:
    print('connect...')
    while not ubit.connected():
        ubit.connect()
    while not ubit.services_resolved():
        lights.set_pixel(1, 1, 255, 0, 0)
        sleep(0.1)
        lights.show()
        lights.clear()
        sleep(0.1)
    print('set up characteristics')
    ubit_btn_b = Characteristic(tools.uuid_dbus_path(
        constants.GATT_CHRC_IFACE,
        'E95DDA90-251D-470A-A062-FA1922DFA9A8')[0])
    ubit_btn_b.add_characteristic_cb(on_button_b)
    ubit_btn_b.start_notify()

    ubit_btn_a = Characteristic(tools.uuid_dbus_path(
        constants.GATT_CHRC_IFACE,
        'E95DDA91-251D-470A-A062-FA1922DFA9A8')[0])
    ubit_btn_a.add_characteristic_cb(on_button_a)
    ubit_btn_a.start_notify()

    ubit_speed = Characteristic(tools.uuid_dbus_path(
        constants.GATT_CHRC_IFACE,
        'E95DFB24-251D-470A-A062-FA1922DFA9A8')[0])
    ubit_speed.write_value((160).to_bytes(2, byteorder='little'))

    ubit_accel = Characteristic(tools.uuid_dbus_path(
        constants.GATT_CHRC_IFACE,
        'E95DCA4B-251D-470A-A062-FA1922DFA9A8')[0])
    ubit_accel.add_characteristic_cb(on_accel_change)
    ubit_accel.start_notify()

    tools.start_mainloop()
