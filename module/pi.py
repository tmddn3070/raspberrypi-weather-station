"""
Weather station pi module
created: 2022-07-13
version: 0.0.1
"""

import os
import requests


def getcputemp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")

def internetcheck(timeout):
    try:
        requests.head("http://naver.com/", timeout=timeout)
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

def restart():
    os.system("sudo reboot")
