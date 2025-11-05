import time

from gevent import monkey
import gevent

# 猴子补丁
monkey.patch_all()

def sing(name):
    for i in range(3):
        # gevent.sleep(1)
        time.sleep(1)
        print(f'{name}"s {i} singing')


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(sing, 'douglas'),
        gevent.spawn(sing, 'anglee'),
    ])

