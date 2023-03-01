from app.devices.DeviceInterface import DeviceInterface
from app.devices.Relay4 import RelayInterface
from app.sensors.Thermometer import Thermometer


class Heater(DeviceInterface):
    def __init__(self, **kwargs):
        self.relay: RelayInterface = kwargs.get('relay')
        self.thermometer: Thermometer = kwargs.get('thermometer')
        super().__init__(**kwargs)

    def on(self):
        self.relay.on()
