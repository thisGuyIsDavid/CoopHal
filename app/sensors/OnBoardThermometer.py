import os, time
from app.utils import is_on_raspberry_pi
from app.devices.DeviceInterface import DeviceInterface


class OnBoardThermometer(DeviceInterface):

    def set_device(self):
        if is_on_raspberry_pi():
            import smbus
            self.device = smbus.SMBus(1)

    def get_temperature(self) -> int:
        self.device.write_i2c_block_data(0x44, 0x2C, [0x06])
        time.sleep(1)
        data = self.device.read_i2c_block_data(0x44, 0x00, 6)
        temp = data[0] * 256 + data[1]
        temperature = -49 + (315 * temp / 65535.0)
        return temperature