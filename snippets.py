from colour import Color
from time import sleep
from modules.breathe import Breathe
import temperature
import datetime

def rgbSolid(ledString, wait):
	patSolid(ledString, [Color('red'),Color('green'), Color('blue')], wait)

def patSolid(ledString, colorArray, wait):
	for color in colorArray:
		ledString.fill(color)
		sleep(wait)

def rgbFill(ledString, wait):
	patFill(ledString, [Color('red'),Color('green'), Color('blue')], wait)

def patFill(ledString, colors, wait):
	for n in range(len(colors)):
		for i in range(int(ledString.num_leds / len(colors))):
			for b in range(len(colors)):
				ledString.put(colors[b], i*len(colors) + ((n+b) if (n+b) < len(colors) else (n-(len(colors)-b))), False)
		ledString.write()
		sleep(wait)

def something(ledString):
	pos = 0
	for i in list(Color('violet').range_to(Color('red'),30)):
		ledString.put(i, pos, False)
		pos += 1
	ledString.write()

def colorFade(ledString, start, end, steps, wait):
	for i in list(start.range_to(end, steps)):
		ledString.fill(i)
		sleep(wait)
	for i in list(end.range_to(start, steps)):
		ledString.fill(i)
		sleep(wait)

def rainbowRotate(ledString, wait):
	rainbow = list(Color('violet').range_to(Color('red'),30))
	for i in range(0,29):
		for n in range(0,30):
			temp = (n+i)%29 if (n+i)>29 else (n+i)
			ledString.put(rainbow[temp], n, False)
		ledString.write()
		sleep(wait)

def travel(ledString, color, wait):
	b = Color('black')
	for i in range(0, ledString.num_leds - 1):
		ledString.put(b, i)
		if i is 0:
			ledString.put(b, ledString.num_leds - 1)
		ledString.put(color, i+1)
		sleep(wait)

def breathe(ledString, color, static=True):
	b = Breathe()
	c = color
	# r = list(Color('blue').range_to(Color('red'),40))

	while True:
		note = 0
		if not static:
			temp = temperature.get_CPU_Core()
			try:
				b.change(temp)
			except TypeError:
				print("Failed to get temperature!")
				exit()
			# if temp < 30:
			# 	c = Color('blue')
			# elif temp > 69:
			# 	c = Color('red')
			# else:
			# 	c = r[int(temp-30)]

		while note < 40:
			c.luminance = (b.move()*0.5)
			ledString.fill(c)
			sleep(0.05)
			note += 1