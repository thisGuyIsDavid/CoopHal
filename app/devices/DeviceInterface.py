

class DeviceInterface:

    def __init__(self, **kwargs):
        self.device = None
        self.name = kwargs.get('name')
        self.set_device()

    def set_device(self):
        pass
