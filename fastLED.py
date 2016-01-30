import serial
from colour import Color
from time import sleep
import atexit

num_leds = 60

class fastLED:
	def __init__(self):
		self.ser = serial.Serial('COM4', 115200)
		self.leds = [0] * (num_leds * 3)
		atexit.register(self.close)

	def write(self):
		self.ser.write(bytes(self.leds))

	def put(self, color, pixel):
		self.leds[pixel * 3] = int(color.red * 256)
		self.leds[pixel * 3 + 1] = int(color.green * 256)
		self.leds[pixel * 3 + 2] = int(color.blue * 256)

	def fill(self, color):
		self.leds = [int(color.red * 255), int(color.green * 255), int(color.blue * 255)] * num_leds
		self.write()

	def close(self):
		self.fill(Color('black'))
		self.write()
		self.ser.close()

a = fastLED()
a.fill(Color('black'))
# a.put(Color('purple'), 3)
# a.write()
# sleep(1)
# a.put(Color('black'), 3)
# a.write()
# sleep(1)
while True:
	for i in list(Color('black').range_to(Color('white'), 50)):
		a.fill(i)
	for i in list(Color('white').range_to(Color('black'), 50)):
		a.fill(i)
a.close()