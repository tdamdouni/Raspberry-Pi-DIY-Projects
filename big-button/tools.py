from pydbus import SystemBus

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

bus = SystemBus()

mngr = bus.get('org.bluez', '/')


def _get_dbus_path(objects, parent_path, iface_in, prop, value):
    for path, iface in objects.items():
        props = iface.get(iface_in)
        if props is None:
            continue
        if props[prop].lower() == value.lower() and path.startswith(parent_path):
            return path


def _add_uuid_dashes(uuid):
    return '{0}-{1}-{2}-{3}-{4}'.format(uuid[0:8], uuid[8:12],
                                        uuid[12:16], uuid[16:20], uuid[20:])


def txt_to_hex(letters):
    return [ord(letter) for letter in letters]


def print_facing(iface, props, invalidated):
    if 'Value' in props:
        val = int.from_bytes(props['Value'][4:], byteorder='little', signed=True)
        if val > 0:
            print('Face down!')
        else:
            print('Face up!')


def _valid_character(char):
    pass


def _valid_uuid(uuid):
    if len(uuid) == 32:
        return _add_uuid_dashes(uuid)
    elif len(uuid) == 4:
        return '0000{0}-0000-1000-8000-00805F9B34FB'.format(uuid)
    else:
        return uuid


def get_dbus_path(device=None, service=None, characteristic=None,
                  descriptor=None, adapter=None):
    mngd_objs = mngr.GetManagedObjects()

    if adapter is None:
        _adt_path = '/org/bluez/hci0'
    else:
        _adt_path = _get_dbus_path(mngd_objs, '/org/bluez',
                                   ADAPTER_INTERFACE, 'Address', adapter)
    if device is None:
        return _adt_path
    else:
        _dev_path = _get_dbus_path(mngd_objs, _adt_path,
                                   DEVICE_INTERFACE, 'Address', device)
    if service is None:
        return _dev_path
    else:
        _srv_path = _get_dbus_path(mngd_objs, _dev_path,
                                   GATT_SERVICE_IFACE, 'UUID', _valid_uuid(service))
    if characteristic is None:
        return _srv_path
    else:
        _chr_path = _get_dbus_path(mngd_objs, _srv_path,
                                   GATT_CHRC_IFACE, 'UUID', _valid_uuid(characteristic))
    if descriptor is None:
        return _chr_path
    else:
        _dsr_path = _get_dbus_path(mngd_objs, _chr_path,
                                   GATT_DESC_IFACE, 'UUID', _valid_uuid(descriptor))
    return _dsr_path
