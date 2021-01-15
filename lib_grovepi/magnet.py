# magnet.py
from lib_grovepi.defcom import *

def initmagnet(pin):
	pinMode(pin,"OUTPUT")
	return 1 

def setmagnet(pin, value):
	digitalWrite(pin,value)
	return 1

def onmagnet(pin):
	digitalWrite(pin,1)
	return 1

def offmagnet(pin):
	digitalWrite(pin,0)
	return 1