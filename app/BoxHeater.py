from simple_pid import PID
from app.devices import Fan
from app.devices import LeftRelay
from app.devices import Thermometer


class BoxHeater:
    TEMP_TO_MAINTAIN = 50

    def __init__(self, fan: Fan, heat_bar: LeftRelay, thermometer: Thermometer):
        self.fan = fan
        self.heat_bar = heat_bar
        self.thermometer = thermometer

        self.pid = PID(5, 0.01, 0.1, setpoint=self.TEMP_TO_MAINTAIN)
        self.pid.output_limits = (0, 1)

    def update(self, boiler_power) -> int:
        if boiler_power == 1:
            self.heat_bar.on()
        else:
            self.heat_bar.off()
        return self.thermometer.get_temperature()

    def set_from_temp(self, dummy_temperature: int = None):
        #   Get the current temperature

        if dummy_temperature is not None:
            current_temperature = dummy_temperature
        else:
            current_temperature = self.thermometer.get_temperature()

        power_status = self.pid(current_temperature)

        if power_status == 1:
            self.heat_bar.on()
        else:
            self.heat_bar.on()

    def run(self):
        pass

if __name__ == '__main__':
    BoxHeater(
        fan=Fan(),
        heat_bar=LeftRelay(),
        thermometer=Thermometer()
    )
