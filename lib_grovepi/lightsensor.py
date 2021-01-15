from lib_grovepi.defcom import *

def initlightsensor(pin):
	pinMode(pin,"INPUT")
	return 1 

def readlightsensor(pin):
	return analogRead(pin)

def reslightsensor(pin):
	# Get sensor value
	sensor_value = analogRead(light_sensor)
	# Calculate resistance of sensor in K
	resistance=-1
	if sensor_value != 0: 
		resistance = (float)(1023 - sensor_value) * 10 / sensor_value
	return resistance