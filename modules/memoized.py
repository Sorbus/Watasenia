'''
Cache calls to a function, to reduce computation time.
'''

from functools import wraps

# cache calls if possible, to reduce computation time
def memoized(f):
	cache = {}
	@wraps(f)
	def wrapped(*args):
		try:
			result = cache[args]
		except KeyError:
			result = cache[args] = f(*args)
		return result
	return wrapped

@memoized
def f():
	pass