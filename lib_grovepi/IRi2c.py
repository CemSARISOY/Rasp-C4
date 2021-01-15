from lib_grovepi.defcom import *

ADDR = 0x5b
EEPROM = 0x10
RAM = 0x20

TA = 0x06
TO = 0x07

PWM_TMIN__SMBUS_SA = 0x00
PWM_T_RANGE = 0x01
CONFIG = 0x02
EMISSIVITY = 0x03


def read_eeprom():
	res =  bus.read_i2c_block_data(ADDR, CONFIG | EEPROM, 3)
	return (res[1] * 256 + res[2])

def read_temp(reg):	
	a,b = bus.read_i2c_block_data(ADDR, reg | RAM, 2)
	temp = int(hex(b) + hex(a)[2:], 16)
	
	temp *= .02 
	temp  -= 273.15
	return round(temp, 2)

def readTO():
	return read_temp(TO)

def readTA():
	return read_temp(TA)