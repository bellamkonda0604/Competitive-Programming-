# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

import math
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	# s1 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
	# s2 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
	# s3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
	s1 = (int(pow((x2 - x1), 2)) + int(pow((y2 - y1), 2)))
	s2 = (int(pow((x3- x1), 2)) + int(pow((y3 - y1), 2)))
	s3 = (int(pow((x3- x2), 2)) + int(pow((y3 - y2), 2)))

	# s = max (s1,s2,s3)
	# if( s == s1):
	# 	return	s1 ** 2 == s3 ** 2 + s2 ** 2
	# elif( s == s2):
	# 	return	s2 ** 2 == s3 ** 2 + s1 ** 2
	# elif( s == s3):
	# 	return	s3 ** 2 == s1 ** 2 + s2 ** 2
	# return 0
	if (s1 > 0 and s2 > 0 and s3 > 0) and (s1 == (s2 + s3) or s2 == (s1 + s3) or s3 == (s2 + s1)):
		return True
	return False