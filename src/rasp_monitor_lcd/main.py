# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division

import os
import sys
import time
import Adafruit_DHT
import read_cqi
import lcd

PIN = 4

lcd.init_lcd()


def get_humidity_and_temperature():
    while 1:
        try:
            h, t = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, PIN)
        except:
            continue
        if t and h:
            return '{}, {}'.format(h, t)


def get_cqi():
    while 1:
        data = read_cqi.read_data()
        if data:
            return '{}, {}, {}'.format(data[str(read_cqi.P_C_PM10)], data[str(read_cqi.P_C_PM25)], data[str(read_cqi.P_C_PM100)])

if __name__ == '__main__':

    pid = os.fork()

    if pid:
        # parent process, exit
        sys.exit(0)

    # child process

    os.umask(0)
    os.setsid()

    while 1:
        lcd.lcd_string('Reading h&t', lcd.LCD_LINE_1)
        line1 = get_humidity_and_temperature()
        lcd.lcd_string('Reading CQI...', lcd.LCD_LINE_2)
        line2 = get_cqi()
        lcd.lcd_string(line1, lcd.LCD_LINE_1)
        lcd.lcd_string(line2, lcd.LCD_LINE_2)

        time.sleep(30)
