from app.interfaces.DeviceInterface import DeviceInterface


class DummyDevice(DeviceInterface):
    value = False

    def on(self):
        self.value = 1

    def off(self):
        self.value = 0


class RelayInterface(DeviceInterface):

    def __init__(self, **kwargs):
        self.pin_number: int = kwargs.get('pin_number')
        super().__init__(**kwargs)

    def set_device(self):
        if self.is_on_pi:
            from gpiozero import DigitalOutputDevice
            self.device = DigitalOutputDevice(self.pin_number, active_high=False, initial_value=True)
            self.off()
        else:
            self.device = DummyDevice()

    def on(self):
        self.database.record_value('relay', self.name, 'on')
        self.device.on()

    def off(self):
        self.database.record_value('relay', self.name, 'off')
        self.device.off()

    def get_status(self) -> bool:
        """
        :return: True if relay is on/active/current is flowing, False if relay is off/inactive/current_is_not_flowing.
        """
        return self.device.value == 1
