import os
import dbus

class FooApp(object):
    def __init__(self):
        if os.environ.get('DBUS_SYSTEM_BUS_ADDRESS'):
            self._bus = dbus.bus.BusConnection(os.environ['DBUS_SYSTEM_BUS_ADDRESS'])
        else:
            self._bus = dbus.SystemBus()
