"""
Weather station upload thingspeak module
created: 2022-07-13
version: 0.0.1
"""
import os
import requests
from config import *

def thingspeak(apikey,temperature,humidity,rainfall,lux,finedust1,finedust25,finedust10,cputemperature):
    url = "https://api.thingspeak.com/update?api_key="+apikey
    url = url + "&field1="+temperature
    url = url + "&field2="+humidity
    url = url + "&field3="+rainfall
    url = url + "&field4="+lux
    url = url + "&field5="+finedust1
    url = url + "&field6="+finedust25
    url = url + "&field7="+finedust10
    url = url + "&field8="+cputemperature
    response = requests.get(url)
    return response.text