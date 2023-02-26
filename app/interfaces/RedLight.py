import time

from app.devices.DeviceInterface import DeviceInterface


class RedLight(DeviceInterface):

    def set_device(self):
        if not self.is_on_pi:
            return
        from gpiozero import PWMLED
        print('PWM light.')
        self.device = PWMLED(12)
        self.device.on()
        time.sleep(2)
        self.device.off()

