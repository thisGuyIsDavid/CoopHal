from app.devices.DeviceInterface import DeviceInterface
from app.utils import is_on_raspberry_pi


class DummyDevice(DeviceInterface):
    value = False

    def on(self):
        self.value = 1

    def off(self):
        self.value = 0


class RelayInterface(DeviceInterface):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pin_number: int = kwargs.get('pin_number')

    def set_device(self):
        if is_on_raspberry_pi():
            from gpiozero import DigitalOutputDevice
            self.device = DigitalOutputDevice(self.pin_number, active_high=False, initial_value=True)
        else:
            self.device = DummyDevice()

    def on(self):
        self.device.on()

    def off(self):
        self.device.off()

    def get_status(self) -> bool:
        """
        :return: True if relay is on/active/current is flowing, False if relay is off/inactive/current_is_not_flowing.
        """
        return self.device.value == 1
