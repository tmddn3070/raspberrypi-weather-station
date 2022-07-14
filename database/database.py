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
            pms_pm1_0 INTEGER NOT NULL,
            pms_pm2_5 INTEGER NOT NULL,
            pms_pm10 INTEGER NOT NULL,
            dht_temp REAL NOT NULL,
            dht_humidity REAL NOT NULL,
            lux FIXED NOT NULL,
            rain BOOLEAN NOT NULL,
            cputemp FIXED NOT NULL,
            timestamp DATETIME NOT NULL,
            warning NULL, 
            cridical NULL
        )
    """)
    db.commit()
    db.close()
    return db

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
    return db
