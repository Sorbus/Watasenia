'''
simple sine wave

well, cosine wave
'''

from memoized import memoized
from patterns import Intensity
import math

class Sine(Intensity):
	def __init__(self):
		Intensity.__init__(self) # inheritance

	@memoized
	def curve(self, x, n):
		return (math.cos(x*math.pi/(1000*n)) / 2) + 0.5

	'''
	The curve used is a logarithmic fit to {{25,1.0},{50,0.5},{80,0.25}}:
		3.07996 - 0.650564 * log(x)
	'''
	def scale(self, temp):
		return 3.07996 - 0.650564 * math.log(temp)