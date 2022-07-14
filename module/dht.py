"""
Weather station DHT22 sensor module
created: 2022-07-05
version: 0.0.1

"""
import RPi.GPIO
import Adafruit_DHT

def getdhtsensor():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    return humidity, temperature

def checkdht():
    humidity, temperature = getdhtsensor()
    if humidity is not None and temperature is not None:
        return "DHTOK"
    else:
        return "DHTKO"