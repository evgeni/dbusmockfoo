import dbus

class FooTwo(object):
    def __init__(self):
        self._system_bus = dbus.SystemBus()

    def numsessions(self):
        logind = self._system_bus.get_object('org.freedesktop.login1', '/org/freedesktop/login1')
        sessions = logind.ListSessions(dbus_interface='org.freedesktop.login1.Manager')
        return len(sessions)
