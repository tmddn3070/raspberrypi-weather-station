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
if internet == True:
    print("Internet is OK")
elif internet == False:
    print("Internet is KO")
else:
    print("Unkown Internet Error")
#check pms
if pmscheck == True:
    print("PMS is OK")
elif pmscheck == False:
    print("PMS is KO")
    sys.exit(0)
else:
    print("pms unkown error")
#check dht
checkdht = checkdht()
if checkdht == True:
    print("DHT is OK")
elif checkdht == False:
    print("DHT is KO")
    sys.exit(0)
else:
    print("dht unkown error")
    sys.exit(0)
#check lux
if luxcheck == True:
    print("LUX is OK")
elif luxcheck == False:
    print("LUX is KO")
    sys.exit(0)
else:
    print("lux unkown error")
#check rain
if rain == True:
    print("rain is OK")
elif rain == False:
    print("rain is KO")
    sys.exit(0)
else:
    print("rain unkown error")
#check cpu
if cputemp == True:
    print("CPU is OK")
elif cputemp == False:
    print("CPU is KO")
    sys.exit(0)
    time.sleep(10)
    restart()
else:
    print("cpu unkown error")
#check database
if os.path.isfile(databasename):
    print("database is OK")
elif not os.path.isfile(databasename):
    print("database is KO")
    os.touch("weather.db")
else:
    print("database unkown error")
#check database
if internet == True and pmscheck == True and checkdht == True and luxcheck == True and raincheck == True:
    print("all is OK")
else:
    print("check failed!")
    
#print status
print(f"sensors: temp:{temperature}, humi:{humidity}, cputemp:{cputemp}, lux:{lux}, rain:{rain}, pms:{pmsval}")
print(f"database:{databasename}")

