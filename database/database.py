import sqlite3
from datetime import datetime
from config import *

def setupdb():
    db = sqlite3.connect(database.database['databasename'])
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            pms_pm1_0 REAL NOT NULL,
            pms_pm2_5 REAL NOT NULL,
            pms_pm10 REAL NOT NULL,
            dht_temp REAL NOT NULL,
            dht_humidity REAL NOT NULL,
            cputemp FLOAT NOT NULL,
            time DATETIME NOT NULL
        )
    """)
    db.commit()
    db.close()
    
def initdblog():
    db = sqlite3.connect(database.database['databasename'])
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS log(
            log STRING NOT NULL,
            time DATETIME NOT NULL
    """)
    db.commit()
    db.close()  

def insertdata(pm1,pm25,pm10,dhttemp,dhthumidity,cputemp,timestamp):
    db = sqlite3.connect(database.database['databasename'])
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO weather (
            pms_pm1_0,
            pms_pm2_5,
            pms_pm10,
            dht_temp,
            dht_humidity,
            cputemp,
            time
        ) VALUES (?,?,?,?,?,?,?)
    """, (pm1,pm25,pm10,dhttemp,dhthumidity,cputemp,timestamp,))
    db.commit()
    db.close()
    return db

def insertlog(log):
    db = sqlite3.connect(database.database['databasename'])
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO log (
            log
            datetime
        ) VALUES (?,?)
    """, (log,datetime.now()))
    db.commit()
    db.close()



