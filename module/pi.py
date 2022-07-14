"""
Weather station pi module
created: 2022-07-13
version: 0.0.1
"""

import os
import requests
import urllib3
def getcputemp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")

def internetcheck(timeout):
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        return "OK"
    except requests.ConnectionError:
        return "KO"

def check_cpu_temp():
    temp = getcputemp()
    if temp > 70:
        return "CPUTEMPKO"
    else:
        return "CPUTEMPOK"


def aptupdate():
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get upgrade -y")
    os.system("sudo apt-get dist-upgrade -y")
    os.system("sudo apt-get autoremove -y")
    os.system("sudo apt-get autoclean -y")
    os.system("sudo apt-get clean -y")

def restart():
    os.system("sudo reboot")

#def thingspeak(apikey,field1,field2,field3,field4,field5,field6,field7,field8):
    #url = "https://api.thingspeak.com/update?api_key="+apikey
    #url = url + "&field1="+field1
    #url = url + "&field2="+field2
    #url = url + "&field3="+field3
    #url = url + "&field4="+field4
    #url = url + "&field5="+field5
   # url = url + "&field6="+field6
   # url = url + "&field7="+field7
   # url = url + "&field8="+field8
   # response = requests.get(url)
   # return response.text