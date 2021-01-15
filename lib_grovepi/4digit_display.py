from lib_grovepi.defcom import *


# Grove 4 Digit Display commands
# Initialise
fourDigitInit_cmd = [70]
# Set brightness, not visible until next cmd
fourDigitBrightness_cmd = [71]
# Set numeric value without leading zeros
fourDigitValue_cmd = [72]
# Set numeric value with leading zeros
fourDigitValueZeros_cmd = [73]
# Set individual digit
fourDigitIndividualDigit_cmd = [74]
# Set individual leds of a segment
fourDigitIndividualLeds_cmd = [75]
# Set left and right values with colon
fourDigitScore_cmd = [76]
# Analog read for n seconds
fourDigitAnalogRead_cmd = [77]
# Entire display on
fourDigitAllOn_cmd = [78]
# Entire display off
fourDigitAllOff_cmd = [79]

# Grove 4 Digit Display - initialise
def fourDigit_init(pin):
	write_i2c_block(address, fourDigitInit_cmd + [pin, unused, unused])
	return 1

# Grove 4 Digit Display - set numeric value with or without leading zeros
# value: (0-65535) or (0000-FFFF)
def fourDigit_number(pin, value, leading_zero):
	# split the value into two bytes so we can render 0000-FFFF on the display
	byte1 = value & 255
	byte2 = value >> 8
	# separate commands to overcome current 4 bytes per command limitation
	if (leading_zero):
		write_i2c_block(address, fourDigitValue_cmd + [pin, byte1, byte2])
	else:
		write_i2c_block(address, fourDigitValueZeros_cmd + [pin, byte1, byte2])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - set brightness
# brightness: (0-7)
def fourDigit_brightness(pin, brightness):
	# not actually visible until next command is executed
	write_i2c_block(address, fourDigitBrightness_cmd + [pin, brightness, unused])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - set individual segment (0-9,A-F)
# segment: (0-3)
# value: (0-15) or (0-F)
def fourDigit_digit(pin, segment, value):
	write_i2c_block(address, fourDigitIndividualDigit_cmd + [pin, segment, value])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - set 7 individual leds of a segment
# segment: (0-3)
# leds: (0-255) or (0-0xFF) one bit per led, segment 2 is special, 8th bit is the colon
def fourDigit_segment(pin, segment, leds):
	write_i2c_block(address, fourDigitIndividualLeds_cmd + [pin, segment, leds])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - set left and right values (0-99), with leading zeros and a colon
# left: (0-255) or (0-FF)
# right: (0-255) or (0-FF)
# colon will be lit
def fourDigit_score(pin, left, right):
	write_i2c_block(address, fourDigitScore_cmd + [pin, left, right])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - display analogRead value for n seconds, 4 samples per second
# analog: analog pin to read
# duration: analog read for this many seconds
def fourDigit_monitor(pin, analog, duration):
	write_i2c_block(address, fourDigitAnalogRead_cmd + [pin, analog, duration])
	time.sleep(duration + .05)
	return 1

# Grove 4 Digit Display - turn entire display on (88:88)
def fourDigit_on(pin):
	write_i2c_block(address, fourDigitAllOn_cmd + [pin, unused, unused])
	time.sleep(.05)
	return 1

# Grove 4 Digit Display - turn entire display off
def fourDigit_off(pin):
	write_i2c_block(address, fourDigitAllOff_cmd + [pin, unused, unused])
	time.sleep(.05)
	return 1