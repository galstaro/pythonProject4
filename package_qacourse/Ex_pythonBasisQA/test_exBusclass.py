from unittest import TestCase, mock
from unittest.mock import patch
from exBusclass import *


class TestBus(TestCase):
    def setUp(self):
        print("setUp")
        self.bus=Bus()
    @mock.patch('exBusclass.Bus.constructor', input_value='gall')
    def test_constructor(self,mock_constractor):

        self.fail()

    def test_get_on(self):
        self.fail()

    def test_get_off(self):
        self.fail()
