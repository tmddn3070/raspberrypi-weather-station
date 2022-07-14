"""
Weather station database module
created: 2022-07-12
version: 0.0.1
"""
import sqlite3
from config import *

def initdb():
    db = sqlite3.connect(database.database['databasename'])
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            pms_pm1_0 FLOAT NOT NULL,
            pms_pm2_5 FLOAT NOT NULL,
            pms_pm10 FLOAT NOT NULL,
            dht_temp FLOAT NOT NULL,
            dht_humidity FLOAT NOT NULL,
            lux FLOAT NOT NULL,
            rain BOOLEAN NOT NULL,
            cputemp INTEGER NOT NULL,
            timestamp DATETIME NOT NULL,
            warning INTEGER NULL, 
            cridical INTEGER NULL
        )
    """)
    db.commit()
    db.close()

def insertdata(pm1,pm25,pm10,dhttemp,dhthumidity,lux,rain,cputemp,timestamp):
    db = sqlite3.connect(database.database['databasename'])
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO weather (
            pms_pm1_0,
            pms_pm2_5,
            pms_pm10,
            dht_temp,
            dht_humidity,
            lux,
            rain,
            cputemp,
            timestamp
        ) VALUES (?,?,?,?,?,?,?,?,?)
    """, (pm1,pm25,pm10,dhttemp,dhthumidity,lux,rain,cputemp,timestamp))
    db.commit()
    db.close()
