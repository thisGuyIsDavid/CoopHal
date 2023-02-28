from app.devices.DeviceInterface import DeviceInterface
import os
import glob
import time


class ProbeInterface(DeviceInterface):
    BASE_DIR = '/sys/bus/w1/devices/'

    def __init__(self, **kwargs):
        self.probe_address: str = kwargs.get('probe_address')
        super().__init__(**kwargs)

    def set_device(self):
        self.device = self.BASE_DIR + self.probe_address + '/w1_slave'

    def get_raw(self):
        with open(self.device) as raw_temp:
            return raw_temp.readlines()

    def get_temperature(self) -> int:
        raw_rows = self.get_raw()
        #   Ensure probe is up and reporting.
        if raw_rows[0].strip()[-3:] != 'YES':
            return -999
        #   Temp row is the second row
        raw_temp_row: str = raw_rows[1].strip()
        raw_temp_value: str = raw_temp_row[raw_temp_row.find('t='):]
        print(raw_temp_value)
        return 3
        pass
