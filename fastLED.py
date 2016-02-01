import serial
from colour import Color
from time import sleep
import atexit

num_leds = 60

class fastLED:
	def __init__(self):
		self.ser = serial.Serial('COM4', 57600, timeout = 1)
		self.leds = [0] * (num_leds * 3)
		atexit.register(self.close)

	def write(self):
		self.ser.write(bytes([65] + self.leds))
		sleep(0.005)

	def put(self, color, pixel, write=True):
		self.leds[pixel * 3] = int(color.red * 255)
		self.leds[pixel * 3 + 1] = int(color.green * 255)
		self.leds[pixel * 3 + 2] = int(color.blue * 255)
		if write:
			self.ser.write(bytes([80, pixel, int(color.red * 255), int(color.green * 255), int(color.blue * 255)]))
			sleep(0.005)

	def fill(self, color, write=True):
		self.leds = [int(color.red * 255), int(color.green * 255), int(color.blue * 255)] * num_leds
		if write:
			self.ser.write(bytes([70, int(color.red * 255), int(color.green * 255), int(color.blue * 255)]))
			sleep(0.005)

	def close(self):
		self.fill(Color('black'))
		self.write()
		self.ser.close()

a = fastLED()
sleep(2)
a.fill(Color('blue'))
sleep(1)
a.fill(Color('red'))
sleep(1)
a.fill(Color('blue'))
sleep(1)
a.fill(Color('purple'))
sleep(1)
# a.put(Color('red'), 3)
# a.put(Color('blue'), 4)
# a.put(Color('green'), 5)
# sleep(2)
# a.fill(Color('maroon'))
# sleep(10)
# a.put(Color('purple'), 3)
# a.write()
# sleep(1)
# a.put(Color('black'), 3)
# a.write()
# sleep(1)
# while True:
# 	for i in list(Color('red').range_to(Color('green'), 50)):
# 		sleep(.1)
# 		a.fill(i)
# 	for i in list(Color('green').range_to(Color('red'), 50)):
# 		sleep(.1)
# 		a.fill(i)
while True:
	c = Color('purple')
	b = Color('black')
	for i in range(0,59):
		a.put(b, i)
		if i is 0:
			a.put(b, 59)
		a.put(c, i+1)
		sleep(0.1)