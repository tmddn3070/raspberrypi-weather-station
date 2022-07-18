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
        return True
    else:
        return False

def checkrain():
    rain = getrain()
    if not rain == None:
        return True
    else:
        return False 

def rainintver():
    rain = getrain()
    if rain == True:
        return 1
    elif rain == False:
        return 0
    else:
        return None
