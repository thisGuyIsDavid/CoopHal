import os

def is_on_raspberry_pi():
    return 'raspberrypi' == os.uname().nodename