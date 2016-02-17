from datetime import datetime

class Intensity:
	def __init__(self):
		self.x = 0 # set time to 0
		self.n = 2 # initial n is *always* 2. It should be changed immediately.
		self.time = False

	# the curve which the method follows
	# probably a good idea to always memoize this
	def curve(self, x, n):
		pass

	# computes n for a temperature, which controls the curve's period 
	def scale(self, temp):
		pass

	# Given a number of milliseconds, moves along the curve and returns the new point
	# NOTE: we assume that the period is always 2000n. 
	# If step is not set, figure out how long it's been!
	def move(self, step=-1):
		if step != -1:
			self.x += step
			self.time = datetime.now()
		else:
			if not self.time:
				self.time = datetime.now()
			else:
				new = datetime.now()
				self.x += int((new - self.time).total_seconds()*1000)
				self.time = new
		if self.x > (self.n * 2000):
			self.x -= (self.n * 4000)
		return(round(self.curve(self.x,self.n),3))

	# Given a temperature in celsius:
	#	- changes n to match that temperature
	#	- moves to an appropriate point in the curve to avoid jitteriness
	def change(self, temp):
		if self.n == round(self.scale(temp),3):
			pass
		else:
			key = round(self.curve(self.x, self.n),3)
			self.n = round(self.scale(temp),3)

			if self.x != 0:
				if self.x > 0:
					self.x = self.binSearch(key, 0, 2000 * self.n)
				else:
					self.x = self.binSearch(key, -2000 * self.n, 0)
			else:
				pass

		return(self.x, self.n)

	'''
	Binary search algorithm for equations.
	'''
	def binSearch(self, key, imin, imax):
		if imax < imin: # key not in set!
			return 0
		else:
			imid = round((imin + imax)/2)

			if round(self.curve(imin, self.n), 3) > round(self.curve(imax, self.n), 3):
				if round(self.curve(imid, self.n), 3) < key:
					return self.binSearch(key, imin, imid)
				elif round(self.curve(imid, self.n), 3) > key:
					return self.binSearch(key, imid, imax)
				else:
					return imid

			else:
				if round(self.curve(imid, self.n), 3) > key:
					return self.binSearch(key, imin, imid)
				elif round(self.curve(imid, self.n), 3) < key:
					return self.binSearch(key, imid, imax)
				else:
					return imid

		# if self.curve(imax, self.n) == key or self.curve(imin, self.n) == key:
		# 	return 0
		# elif round(self.curve(imid, self.n),3) < key:
		# 	return self.binSearch(key, imin, imid + 1)
		# elif round(self.curve(imid, self.n),3) > key:
		# 	return self.binSearch(key, imid - 1, imax)
		# else:
		# 	return imid