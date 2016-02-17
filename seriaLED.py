import serial
from colour import Color
from time import sleep
import atexit

class seriaLED:
	def __init__(self, num_leds, wait=True):
		self.ser = serial.Serial('COM4', 57600, timeout = 1)
		self.leds = [0] * (num_leds * 3)
		self.num_leds = num_leds
		atexit.register(self.close)
		if wait:
			sleep(2) # enforced wait for everything to start working.
					 # if there isn't a small wait then some commands can get lost.
					 # can optionally be skipped, which may be appropriate for some use cases.

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
		self.leds = [int(color.red * 255), int(color.green * 255), int(color.blue * 255)] * self.num_leds
		if write:
			self.ser.write(bytes([70, int(color.red * 255), int(color.green * 255), int(color.blue * 255)]))
			sleep(0.005)

	def close(self):
		self.fill(Color('black'))
		self.write()
		self.ser.close()