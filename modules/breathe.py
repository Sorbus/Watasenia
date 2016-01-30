'''
breathing LEDs
based on http://sean.voisen.org/blog/2011/10/breathing-led-with-arduino/

uses the equation:
(e^cos(x*pi/(2000*n)) - 1/e) * ( (e^2-1) / e^2) / (e-(1/e) ) + 0.135
	Maximum: 1
	Minimum: ~0.135
	Period: 2000n
'''

from memoized import memoized
import math

@memoized
def compute(x, n):
	return (math.exp(math.cos(x*math.pi/(2000*n))) - 0.36787 ) * 0.36787 + 0.135

class Breathe:
	def __init__(self):
		self.x = 0
		self.n = 2

	'''
	Given a number of milliseconds, moves along the curve and returns the new point
	'''
	def move(self, step):
		self.x += step
		if self.x > (self.n * 2000):
			self.x -= (self.n * 2000)
		return(round(compute(self.x,self.n),3))

	'''
	Given a temperature in celsius:
		- changes n to match that temperature
		- moves to an appropriate point in the curve to avoid jitteriness

	The curve used is a logarithmic fit to {{25,1.0},{50,0.5},{80,0.25}}:
		3.07996 - 0.650564 * log(x)
	'''
	def change(self, temp):
		key = round(compute(self.x, self.n),2)
		
		if compute(self.x + 1, self.n) > key:
			rising = True
		else:
			rising = False

		self.n = round(3.07996 - 0.650564 * math.log(temp),3)

		if self.x != 0:
			if rising:
				self.x = self.binSearch(key, 0, 2000 * self.n)
			else:
				self.x = (1000 * self.n) - self.binSearch(key, 0, 2000 * self.n)
		else:
			pass

		return(self.x, self.n)

	def binSearch(self, key, imin, imax):
		imid = round((imin + imax)/2)

		if compute(imax, self.n) > key or compute(imin, self.n) < key:
			return 0
		elif round(compute(imid, self.n),3) < key:
			return self.binSearch(key, imin, imid + 1)
		elif round(compute(imid, self.n),3) > key:
			return self.binSearch(key, imid - 1, imax)
		else:
			return imid