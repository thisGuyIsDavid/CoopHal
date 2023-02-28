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
        with open(self.device + '/name') as raw_temp:
            return raw_temp.readlines()

    def get_temperature(self) -> int:
        print(self.get_raw())
        return 3
        pass
