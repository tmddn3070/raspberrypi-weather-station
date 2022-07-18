"""
Weather station scheduler module
created: 2022-07-18
version: 0.0.2
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
from module.bh import *
from module.rain import *
from module.uploadthingspeak import *


def thingspeakjob():
    humidity, temperature = getdhtsensor()
    pmsval1, pmsval2, pmsval10 = getpms()
    thing, err = thingspeak(mainconfig['thingspeak-apikey'],temperature,humidity,rainintver(),getlux(),pmsval1,pmsval2,pmsval10,getcputemp())
    logl(f"{err}")
    
def databasejob():
    humidity, temperature = getdhtsensor()
    pmsval1, pmsval2, pmsval10 = getpms()
    insert = insertdata(pmsval1,pmsval2,pmsval10,temperature,humidity,getlux(),getrain(),getcputemp(),datetime.now())
    insertlogl(f"{insert}") 

def autoupdatejob():
    aptupdate()

def checkcputempjob():
    checkcputemp()


schedule.every(5).minutes.do(thingspeakjob)
schedule.every(2).minutes.do(databasejob)
schedule.every().hour.do(checkcputempjob)
schedule.every().wednesday.at("1:15").do(autoupdatejob)
 

while True:
    schedule.run_pending()
    time.sleep(1)
