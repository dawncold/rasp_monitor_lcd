# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
import read_cqi

CQI_FILE_NAME = 'cqi'

if __name__ == '__main__':
    data = read_cqi.read_data()
    if data:
        with open('/home/pi/{}'.format(CQI_FILE_NAME), mode='wb+') as f:
            f.write('{},{},{}'.format(data[str(read_cqi.P_C_PM10)],
                                      data[str(read_cqi.P_C_PM25)],
                                      data[str(read_cqi.P_C_PM100)]).encode('UTF-8'))
