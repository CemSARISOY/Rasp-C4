# led.py
from lib_grovepi.defcom import *

def initLED(pin):
	pinMode(pin,"OUTPUT")
	return 1 

def setLED(pin, value):
	digitalWrite(pin,value)
	return 1

def onLED(pin):
	digitalWrite(pin,1)
	return 1

def offLED(pin):
	digitalWrite(pin,0)
	return 1