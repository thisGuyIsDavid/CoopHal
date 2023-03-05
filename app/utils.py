import os


def is_on_raspberry_pi():
    return 'raspberrypi' == os.uname().nodename

if __name__ == '__main__':
    import datetime
    import time
    start = datetime.datetime.now()
    time.sleep(4)
    end = datetime.datetime.now()
    print((end - start).seconds / 60)