from app.devices.DeviceInterface import DeviceInterface


class RedLight(DeviceInterface):

    def set_device(self):
        if not self.is_on_pi:
            return
        from gpiozero import PWMLED
        self.device = PWMLED(12)
        self.device.on()

