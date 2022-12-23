import os
import sys
import time
import datetime

import smbus

if 'raspberrypi' == os.uname().nodename:
    from gpiozero import DigitalOutputDevice
else:
    from DummyClasses import DigitalOutputDevice


class SolarMaintainer:

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.heat_bar = DigitalOutputDevice(15, active_high=False, initial_value=True)
        self.turn_off_heat_bar()

        self.fan = DigitalOutputDevice(18, active_high=False, initial_value=True)
        self.turn_off_fan()

        self.collection = None

    def test_fan(self):
        self.turn_off_fan()
        assert not self.get_fan_status()
        time.sleep(5)

        self.turn_on_fan()
        assert self.get_fan_status()
        time.sleep(5)

        self.turn_off_fan()
        assert not self.get_fan_status()
        time.sleep(5)

    def test_heat_bar(self):
        self.turn_off_heat_bar()
        assert not self.get_heat_bar_status()
        time.sleep(5)

        self.turn_on_heat_bar()
        assert self.get_heat_bar_status()
        time.sleep(5)

        self.turn_off_heat_bar()
        assert not self.get_heat_bar_status()
        time.sleep(5)

    def test_relays(self):
        self.test_fan()
        self.test_heat_bar()

    def turn_on_fan(self):
        self.fan.on()
        print('FAN SHOULD BE ON:', self.get_fan_status())

    def turn_off_fan(self):
        self.fan.off()
        print('FAN SHOULD BE OFF:', self.get_fan_status())

    def get_fan_status(self):
        return self.fan.value == 1

    def turn_on_heat_bar(self):
        self.heat_bar.on()
        print('HEAT BAR SHOULD BE ON:', self.get_heat_bar_status())

    def turn_off_heat_bar(self):
        self.heat_bar.off()
        print('HEAT BAR SHOULD BE OFF:', self.get_heat_bar_status())


    def get_heat_bar_status(self):
        return self.heat_bar.value == 1

    def get_temperature_and_humidity(self):
        # SHT31 address, 0x44(68)
        self.bus.write_i2c_block_data(0x44, 0x2C, [0x06])

        time.sleep(1)

        data = self.bus.read_i2c_block_data(0x44, 0x00, 6)

        # Convert the data
        temp = data[0] * 256 + data[1]
        temperature = -49 + (315 * temp / 65535.0)
        humidity = 100 * (data[3] * 256 + data[4]) / 65535.0

        return temperature, humidity

    def run(self):

        seconds_to_record = 900
        sleep_duration = 15
        loop_count = 0
        is_initial = True

        while True:
            temperature, humidity = self.get_temperature_and_humidity()
            mapped = {
                'temperature': round(temperature, 2),
                'humidty': round(humidity, 2),
                'heat_bar_status': 'ON' if self.get_heat_bar_status() else 'OFF',
                'fan_status': 'ON' if self.get_fan_status() else 'OFF',
                'date_of_reading': datetime.datetime.utcnow(),
                'name': 'Solar Panel',
                'sensor': 'internal'
            }

            if is_initial or loop_count > (seconds_to_record / sleep_duration):
                self.collection.add(mapped)
                loop_count = 0
                is_initial = False
            time.sleep(sleep_duration)
            loop_count += 1


if __name__ == '__main__':
    try:
        SolarMaintainer().test_relays()
    except KeyboardInterrupt:
        sys.exit()
