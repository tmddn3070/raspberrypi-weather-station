"""
Weather station rain sensor module
created: 2022-07-13
version: 0.0.1
"""
import os
import RPi.GPIO as io

def getrain():
    water_sensor = 26
    io.setmode(io.BCM)
    io.setup(water_sensor, io.IN)    
    if io.input(water_sensor):
        return "rain"
    else:
        return "no rain"

def checkrain():
    rain = getrain()
    if rain == None:
        return "rainKO"
    else:
        return "rainOK"