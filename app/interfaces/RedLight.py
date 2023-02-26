import time

from app.devices.DeviceInterface import DeviceInterface


class RedLight(DeviceInterface):

    def set_device(self):
        if not self.is_on_pi:
            return
        from gpiozero import PWMLED
        print('PWM light.')
        self.device = PWMLED(12)
        self.device.off()

    def get_status(self) -> bool:
        return self.device.is_lit

    def pulse(self):
        self.device.pulse()

    def on(self):
        self.device.on()

    def off(self):
        self.device.off()
