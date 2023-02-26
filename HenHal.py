from app.sensors import OnBoardThermometer
from app.interfaces import RedLight
import time


class HenHal:

    def __init__(self, **kwargs):
        self.on_board_thermometer: OnBoardThermometer = OnBoardThermometer()
        self.red_light: RedLight = RedLight()

    def run(self):
        while True:
            print(self.on_board_thermometer.get_temperature())
            time.sleep(5)

    def run_hen_hal(self):
        try:
            self.run()
        except KeyboardInterrupt as e:
            return


if __name__ == '__main__':
    HenHal().run_hen_hal()
