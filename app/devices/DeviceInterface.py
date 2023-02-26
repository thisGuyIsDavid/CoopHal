from app.utils import is_on_raspberry_pi


class DeviceInterface:

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.is_on_pi: bool = is_on_raspberry_pi()

        self.device = None
        self.set_device()

    def set_device(self):
        pass
