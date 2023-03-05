from app.interfaces.DeviceInterface import DeviceInterface
from app.devices.Relay4 import RelayInterface
from app.interfaces.ThermometerInterface import ThermometerInterface


class Heater(DeviceInterface):
    def __init__(self, **kwargs):
        self.relay: RelayInterface = kwargs.get('relay')
        self.thermometer: ThermometerInterface = kwargs.get('thermometer')
        super().__init__(**kwargs)

    def on(self):
        self.relay.on()
