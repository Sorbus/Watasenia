'''
breathing LEDs
based on http://sean.voisen.org/blog/2011/10/breathing-led-with-arduino/

uses the equation:
(e^cos(x*pi/(2000*n)) - 1/e) * ( (e^2-1) / e^2) / (e-(1/e) ) + 0.135
	Maximum: 1
	Minimum: ~0.135
	Period: 2000n
'''

from modules.memoized import memoized
from modules.patterns import Intensity
import math

class Breathe(Intensity):
	def __init__(self):
		Intensity.__init__(self) # inheritance

	@memoized
	def curve(self, x, n):
		return (math.exp(math.cos(x*math.pi/(2000*n))) - 0.36787 ) * 0.36787 + 0.135

	'''
	The curve used is a logarithmic fit to {{25,1.0},{50,0.5},{80,0.25}}:
		3.07996 - 0.650564 * log(x)
	'''
	def scale(self, temp):
		return 3.07996 - 0.650564 * math.log(temp)