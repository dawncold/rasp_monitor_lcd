# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
import Adafruit_DHT

PIN = 4
TH_FILE_NAME = 'th'

if __name__ == '__main__':
    t, h = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, PIN)
    if t and h:
        with open(TH_FILE_NAME, mode='wb+') as f:
            f.write('{},{}'.format(t, h).encode('UTF-8'))
