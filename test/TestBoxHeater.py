import unittest
from app.BoxHeater import BoxHeater
from app.devices import Thermometer
from app.devices import LeftRelay
from app.devices import Fan


class DummyThermometer(Thermometer):
    def get_temperature(self) -> int:
        pass


class DummyFan(Fan):
    pass


class DummyHeatBar(LeftRelay):
    pass


class TestBoxHeater(unittest.TestCase):

    def test_pid(self):
        box_heater = BoxHeater(
            thermometer=DummyThermometer(),
            heat_bar=DummyHeatBar(),
            fan=DummyFan()
        )
        box_heater.set_from_temp(40)
        self.assertTrue(box_heater.heat_bar.get_status())





