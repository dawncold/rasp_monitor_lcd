# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division

import time
import Adafruit_DHT
import read_cqi
import lcd

PIN = 4

lcd.init_lcd()


def get_th():
    while 1:
        try:
            t, h = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, PIN)
        except:
            continue
        if t and h:
            return t, h


def get_cqi():
    while 1:
        data = read_cqi.read_data()
        if data:
            return '{},{},{}'.format(data[str(read_cqi.P_C_PM10)], data[str(read_cqi.P_C_PM25)], data[str(read_cqi.P_C_PM100)])


while 1:
    line1 = get_th()
    line2 = get_cqi()
    lcd.lcd_string(line1, lcd.LCD_LINE_1)
    lcd.lcd_string(line2, lcd.LCD_LINE_2)

    time.sleep(30)
