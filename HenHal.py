import time

from app.DataStorage import DataStorage
from app.devices import Relay1, Relay2, Relay3, Relay4
from app.devices.RelayInterface import RelayInterface
from app.interfaces import RedLight
from app.sensors import OnBoardThermometer


class HenHal:

    def __init__(self, **kwargs):
        self.database: DataStorage = DataStorage()
        self.on_board_thermometer: OnBoardThermometer = OnBoardThermometer(database=self.database)
        self.relay_1: RelayInterface = Relay1(
            name='relay 1',
            pin_number=kwargs.get('relay_1'),
            database=self.database
        )
        self.relay_2: RelayInterface = Relay2(
            name='relay 2',
            pin_number=kwargs.get('relay_2'),
            database=self.database
        )
        self.relay_3: RelayInterface = Relay3(
            name='relay 3',
            pin_number=kwargs.get('relay_3'),
            database=self.database
        )
        self.relay_4: RelayInterface = Relay4(
            name='relay 4',
            pin_number=kwargs.get('relay_4'),
            database=self.database
        )
        self.red_light: RedLight = RedLight(database=self.database)

    def run_test(self):
        self.red_light.pulse()
        for relay in [self.relay_1, self.relay_2, self.relay_3, self.relay_4]:
            relay.on()
            time.sleep(1)
            relay.off()
            time.sleep(1)

    def run(self):
        iterations = 0
        while True:
            #   Once every five minutes
            if iterations % 60 == 0:
                self.on_board_thermometer.get_temperature()
                #   Iterations also resets.
                iterations = 0

            #   Once a minute.
            if iterations % 12 == 0:
                self.red_light.check_connection()

            #   Once every thirty seconds.
            if iterations % 6 == 0:
               pass

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
        relay_1=26,
        relay_2=19,
        relay_3=20,
        relay_4=16
    ).run_hen_hal()
