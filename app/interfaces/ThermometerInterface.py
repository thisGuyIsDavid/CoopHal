from app.interfaces.DeviceInterface import DeviceInterface


class ThermometerInterface(DeviceInterface):

    def get_temperature(self) -> float:
        pass

    def record_temperature(self) -> None:
        self.database.record_value(
            'temperature',
            self.name,
            self.get_temperature()
        )
