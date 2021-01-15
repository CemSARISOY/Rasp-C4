
from lib_grovepi.defcom import *


# If you wish to connect two joysticks, for exemple use ports A0 and A2 (skip A1)
# Don't plug anything into port A1 that uses pin 1
# Uses two pins - one for the X axis and one for the Y axis
def initjoystick(pin):
	pinMode(pin,"INPUT")
	pinMode(pin+1,"INPUT")
	return 1 




# My Joystick Specifications
#     Min  Typ  Max  Click
#  X  250  509  772  1020-1023
#  Y  242  516  780

def readjoystick(pin):
	# Get X/Y coordinates
	x = analogRead(pin)
	y = analogRead(pin+1)
	# Was a click detected on the X axis?
	click = 1 if x >= 1020 else 0

	return [x - 509, y - 516, click ]

def resjoystick(pin):
	# Get X/Y coordinates
	x = analogRead(pin)
	y = analogRead(pin+1)

	# Calculate X/Y resistance
	Rx = (float)(1023 - x) * 10 / x
	Ry = (float)(1023 - y) * 10 / y
	return [Rx,Ry]