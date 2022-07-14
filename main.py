"""
Weather station main runtime
created: 2022-07-05
version: 0.0.1
"""
# main module
import os
import sys
import RPi.GPIO
import Adafruit_DHT
import sqlite3

#sensor ext module
from pms7003 import Pms7003Sensor, PmsSensorException
from .config import *
from .module.dht import *
from .module.pi import *
from .module.pms import *
from .database.database import *
from .module.bh import *
from .module.rain import *

#set sensor
humidity, temperature = getdhtsensor()
cputemp = getcputemp()
pms = Pms7003Sensor('/dev/serial0')
pmscheck = checkpms()
pmsval1, pmsval2, pmsval10 = getpms()
lux = getlux()
luxcheck = checklux()
rain = getrain()
raincheck = checkrain()
databasename = database.database['databasename']

#check internet conn
internet = internetcheck(20)
if internet == "OK":
    print("Internet is OK")
elif internet == "KO":
    print("Internet is KO")
else:
    print("Unkown Internet Error")
#check pms
if pmscheck == "PMSOK":
    print("PMS is OK")
elif pmscheck == "PMSKO":
    print("PMS is KO")
else:
    print("pms unkown error")
#check dht
checkdht = checkdht()
if checkdht == "DHTOK":
    print("DHT is OK")
elif checkdht == "DHTKO":
    print("DHT is KO")
else:
    print("dht unkown error")
#check lux
if luxcheck == "LUXOK":
    print("LUX is OK")
elif luxcheck == "LUXKO":
    print("LUX is KO")
else:
    print("lux unkown error")
#check rain
if rain == "rainOK":
    print("rain is OK")
elif rain == "rainKO":
    print("rain is KO")
else:
    print("rain unkown error")
#check cpu
if cputemp == "CPUTEMPOK":
    print("CPU is OK")
elif cputemp == "CPUTEMPKO":
    print("CPU is KO")
else:
    print("cpu unkown error")
#check database
if os.path.isfile(databasename):
    print("database is OK")
elif not os.path.isfile(databasename):
    print("database is KO")
else:
    print("database unkown error")
#check database
if internet == "OK" and pmscheck == "PMSOK" and checkdht == "DHTOK" and luxcheck == "LUXOK" and raincheck == "rainOK":
    print("all is OK")
else:
    print("check failed!")
#print status
print(f"sensors: temp:{temperature}, humi:{humidity}, cputemp:{cputemp}, lux:{lux}, rain:{rain}, pms:{pmsval}")
print(f"database:{databasename}")

