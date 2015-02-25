import os
import dbus

class FooOne(object):
    def __init__(self):
        if os.environ.get('DBUS_SYSTEM_BUS_ADDRESS'):
            self._system_bus = dbus.bus.BusConnection(os.environ['DBUS_SYSTEM_BUS_ADDRESS'])
        else:
            self._system_bus = dbus.SystemBus()

    def numsessions(self):
        logind = self._system_bus.get_object('org.freedesktop.login1', '/org/freedesktop/login1')
        sessions = logind.ListSessions(dbus_interface='org.freedesktop.login1.Manager')
        return len(sessions)
