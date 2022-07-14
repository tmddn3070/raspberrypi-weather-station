"""
Weather station error handling module
created: 2022-07-13
version: 0.0.1
"""
#import sensor module
from pms7003 import Pms7003Sensor, PmsSensorException
from config import *
from dht import *
from pi import *
from pms import *
from database.database import *
from bh import *
from rain import *
#set sensor
humidity, temperature = getdhtsensor(4)
cputemp = getcputemp()
pms = Pms7003Sensor('/dev/serial0')
pmscheck = checkpms()
pmsgab = getpms()
lux = getlux()
luxcheck = checklux()
rain = getrain()
raincheck = checkrain()
databasename = database.database['databasename']
