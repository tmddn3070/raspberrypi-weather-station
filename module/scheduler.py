import os
import sys
from tabnanny import check
import RPi.GPIO
import Adafruit_DHT
import sqlite3
import schedule
import time
from datetime import datetime
#sensor ext module
from pms7003 import Pms7003Sensor, PmsSensorException
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
    thingspeak(mainconfig['thingspeak-apikey'],temperature,humidity,getrain(),getlux(),pmsval1,pmsval2,pmsval10,getcputemp())
    
def databasejob():
    humidity, temperature = getdhtsensor()
    pmsval1, pmsval2, pmsval10 = getpms()
    insertdata(pmsval1,pmsval2,pmsval10,temperature,humidity,getlux(),getrain(),getcputemp(),datetime.now())

def autoupdatejob():
    aptupdate()

def checkcputemp():
    checkcputemp()

schedule.every(5).minutes.do(thingspeakjob)
schedule.every(2).minutes.do(databasejob)
schedule.every().hour.do(checkcputemp)
schedule.every().wednesday.at("1:15").do(autoupdatejob)
 

while True:
    schedule.run_pending()
    time.sleep(1)
