"""
Weather station scheduler module
created: 2022-11-24
version: 0.0.5
"""

import schedule
import time
from datetime import datetime
#sensor ext module
from config import *
from module.dht import *
from module.pi import *
from module.pms import *
from database.database import *
from module.uploadthingspeak import *


def thingspeakjob():
    dht = getdhtsensor()
    pms = getpms()
    try:
        result, log = thingspeak(mainconfig['thingspeak-apikey'],dht[0],dht[1],pms[0],pms[1],pms[2],getcputemp())
    if result == False:
        pass
    elif result == True:
        insertlog(log)
    
def databasejob():
    dht = getdhtsensor()
    pms = getpms()
    insertdata(pms[0],pms[1],pms[2],dht[0],dht[1],getcputemp(),datetime.now())

def autoupdatejob():
    aptupdate()

def checkcputempjob():
    checkcputemp()


schedule.every(1).minutes.do(thingspeakjob)
schedule.every(2).minutes.do(databasejob)
schedule.every().hour.do(checkcputempjob)
schedule.every().wednesday.at("1:15").do(autoupdatejob)
 

while True:
    schedule.run_pending()
    time.sleep(1)
