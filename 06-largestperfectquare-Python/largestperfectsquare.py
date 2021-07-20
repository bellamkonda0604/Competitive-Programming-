# largestPerfectSquare(n) [10 pts]
# Write the function largestPerfectSquare(n) that takes a non-negative int n, and returns  the largest perfect
# square that is no larger than n. For example:
# assert(largestPerfectSquare(24) == 16)
# assert(largestPerfectSquare(25) == 25)
# assert(largestPerfectSquare(26) == 25)
# Hint: you may wish to use a similar approach to how you solved isPerfectSquare on the hw.
# Another hint: This can be written using just one or two lines of Python.

import math

def isperfectsquare(n):
	# your code goes here
	if(type(n) != int):
		return False
	if n > 0:
		n = math.sqrt(n)
		return math.ceil(n) == math.floor(n)
			# return True
	else:
		return False

def largestperfectsquare(n):
	# your code goes here
	if isperfectsquare(n):
		print(n)
		return n
	else:
		# if isperfectsquare((n**0.5)):
		# 	return math.ceil(n)
		x = math.floor(n ** 0.5)
		return x ** 2
# print(largestperfectsquare(24))