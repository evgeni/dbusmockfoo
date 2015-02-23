import unittest
import sys
import dbus
import dbusmock
import subprocess

import dbusmockfoo.fooone

class TestLogind(dbusmock.DBusTestCase):

    @classmethod
    def setUpClass(klass):
        klass.start_system_bus()
        klass.dbus_con = klass.get_dbus(True)

    def setUp(self):
        self.p_mock = None
 
    def tearDown(self):
        if self.p_mock:
            self.p_mock.terminate()
            self.p_mock.wait()

    def test_fooone(self):
        (self.p_mock, obj_logind) = self.spawn_server_template('logind', {}, stdout=subprocess.PIPE)
        x = dbusmockfoo.fooone.FooOne()
        r = x.numsessions()
        self.assertTrue(x)
        self.assertTrue(r == 0)

