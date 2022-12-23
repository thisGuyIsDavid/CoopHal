import os, time
import utils


class Thermometer:

    def __init__(self):
        self.i2c_bus = None
        self.set_sensor()

    def set_sensor(self):
        if utils.is_on_raspberry_pi():
            import smbus
            self.i2c_bus = smbus.SMBus(1)

    def get_temperature(self) -> int:
        self.i2c_bus.write_i2c_block_data(0x44, 0x2C, [0x06])
        time.sleep(1)
        data = self.i2c_bus.read_i2c_block_data(0x44, 0x00, 6)
        temp = data[0] * 256 + data[1]
        temperature = -49 + (315 * temp / 65535.0)
        return temperature

    def get_dummy_temperature(self) -> int:
        return 8

if __name__ == '__main__':
    temperature = Thermometer().get_temperature()
    print(temperature)