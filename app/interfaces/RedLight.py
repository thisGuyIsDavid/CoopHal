import time
import socket
from app.devices.DeviceInterface import DeviceInterface


class RedLight(DeviceInterface):
    """
    On if program is running and connected to the internet.
    """

    def set_device(self):
        if not self.is_on_pi:
            return
        from gpiozero import PWMLED
        print('PWM light.')
        self.device = PWMLED(12)

    def get_status(self) -> bool:
        return self.device.is_lit

    def pulse(self):
        self.device.pulse()

    def on(self):
        self.device.on()

    def off(self):
        self.device.off()

    def check_connection(self):
        self.pulse()
        if self.is_connected():
            self.device.on()
        else:
            self.device.off()

    @staticmethod
    def is_connected(host="8.8.8.8", port=53, timeout=3) -> bool:
        #   https://stackoverflow.com/questions/3764291/how-can-i-see-if-theres-an-available-and-active-network-connection-in-python
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            return False
