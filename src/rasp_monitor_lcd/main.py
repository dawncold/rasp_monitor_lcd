# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division

import time

import save_th
import save_cqi
import lcd

line1 = None
line2 = None


def read_line1():
    with open(save_th.TH_FILE_NAME) as f:
        return f.read()


def read_line2():
    with open(save_cqi.CQI_FILE_NAME) as f:
        return f.read()


lcd.init_lcd()


while 1:
    line1_data = read_line1()
    if line1 is None:
        line1 = line1_data
    elif line1 != line1_data:
        line1 = line1_data

    line2_data = read_line2()
    if line2 is None:
        line2 = line2_data
    elif line2 != line2_data:
        line2 = line2_data

    lcd.lcd_string(line1, lcd.LCD_LINE_1)
    lcd.lcd_string(line2, lcd.LCD_LINE_2)

    time.sleep(15)
