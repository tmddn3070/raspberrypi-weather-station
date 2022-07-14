"""
Weather station pms7003 module
created: 2022-07-13
version: 0.0.1
"""

from pms7003 import Pms7003Sensor, PmsSensorException


def checkpms():
    try:
        pms = Pms7003Sensor('/dev/serial0')
        pms.read()
        return "PMSOK"
    except PmsSensorException:
        return "PMSKO"

def getpms():
    pms = Pms7003Sensor('/dev/serial0')
    pms.read()
    return pms.pm1_0, pms.pm2_5, pms.pm10