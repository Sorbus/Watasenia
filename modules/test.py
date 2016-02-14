# NOTE: should really move to a unit testing framework

import breathe, sine

test = breathe.Breathe()
print(test.move(1414) 	== 0.573)
print(test.move(12)		== 0.568)
print(test.move(12414)	== 0.417)
print(test.change(30)	== (74.000000, 0.867000))
print(test.move(12)		== 0.988)
print(test.change(50)	== (487.000000, 0.535000))
print(test.move(12)		== 0.408)
print(test.change(70)	== (22.000000, 0.316000))
print(test.move(12)		== 0.985)
print(test.change(30)	== (791.000000, 0.867000))
print(test.move(1000)	== 0.994)
print(test.change(25)	== (86.000000, 0.986000))

test = breathe.Breathe()
print(test.change(55)	== (0.0,0.473))

test = sine.Sine()
print(test.move(1414) 	)
print(test.move(12)		)
print(test.move(12414)	)
print(test.change(30)	)
print(test.move(12)		)
print(test.change(50)	)
print(test.move(12)		)
print(test.change(70)	)
print(test.move(12)		)
print(test.change(30)	)
print(test.move(1000)	)
print(test.change(25)	)