import dbus

class FooApp(object):
    def __init__(self):
        self._bus = dbus.SystemBus()
