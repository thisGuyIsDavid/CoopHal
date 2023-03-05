import time

from app.interfaces.ThermometerInterface import ThermometerInterface


class OnBoardThermometer(ThermometerInterface):

    def set_device(self):
        if self.is_on_pi:
            import smbus
            self.device = smbus.SMBus(1)

    def get_temperature(self) -> float:
        if not self.is_on_pi:
            return -999
        self.device.write_i2c_block_data(0x44, 0x2C, [0x06])
        time.sleep(1)
        data = self.device.read_i2c_block_data(0x44, 0x00, 6)
        temp = data[0] * 256 + data[1]
        temperature = -49 + (315 * temp / 65535.0)
        temperature = round(temperature, 2)
        return temperature
