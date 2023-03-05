from app.interfaces.ThermometerInterface import ThermometerInterface


class ProbeInterface(ThermometerInterface):
    BASE_DIR = '/sys/bus/w1/devices/'

    def __init__(self, **kwargs):
        self.probe_address: str = kwargs.get('probe_address')
        super().__init__(**kwargs)

    def set_device(self):
        self.device = self.BASE_DIR + self.probe_address + '/w1_slave'

    def get_raw(self):
        with open(self.device) as raw_temp:
            return raw_temp.readlines()

    def get_temperature(self) -> float:
        raw_rows = self.get_raw()
        #   Ensure probe is up and reporting.
        if raw_rows[0].strip()[-3:] != 'YES':
            return -999
        #   Temp row is the second row
        raw_temp_row: str = raw_rows[1].strip()
        raw_temp_value: str = raw_temp_row[raw_temp_row.find('t=') + 2:]

        #   ensure it's an integer.
        try:
            temp_value: int = int(raw_temp_value)
        except ValueError:
            return -999

        temp_in_celsius = float(temp_value) / 1000.0
        temp_in_fahrenheit = temp_in_celsius * 9.0 / 5.0 + 32.0
        return temp_in_fahrenheit


if __name__ == '__main__':
    int('wor')