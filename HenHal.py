from app.sensors import OnBoardThermometer
from app.interfaces import RedLight
from app.devices import LeftRelay, RightRelay
from app.devices.RelayInterface import RelayInterface
import time


class HenHal:

    def __init__(self, **kwargs):
        self.on_board_thermometer: OnBoardThermometer = OnBoardThermometer()
        self.left_relay: RelayInterface = LeftRelay(pin_number=kwargs.get('left_relay'))
        self.right_relay: RelayInterface = RightRelay(pin_number=kwargs.get('right_relay'))
        self.red_light: RedLight = RedLight()

    def run_test(self):
        self.red_light.pulse()
        self.left_relay.on()
        time.sleep(1)
        self.left_relay.off()
        time.sleep(1)
        self.right_relay.on()
        time.sleep(1)
        self.right_relay.off()
        time.sleep(1)

    def run(self):
        iterations = 0
        while True:
            #   Once a minute.
            if iterations % 12 == 0:
                self.red_light.check_connection()
                #   Iterations also resets once a minute.
                iterations = 0

            #   Once every thirty seconds.
            if iterations % 6 == 0:
                self.on_board_thermometer.get_temperature()

            time.sleep(5)
            iterations += 1

    def run_hen_hal(self):
        try:
            self.run_test()
            self.run()
        except KeyboardInterrupt as e:
            return
        finally:
            self.red_light.off()


if __name__ == '__main__':
    HenHal(
        left_relay=16,
        right_relay=20
    ).run_hen_hal()
