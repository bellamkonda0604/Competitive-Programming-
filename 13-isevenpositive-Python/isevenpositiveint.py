# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
	# your code goes here
	if type(x) == list:
		return False
	if type(x) == str:
		return False
	if type(x) == tuple:
		return False
	if type(x) == int and x > 0 and x % 2 == 0:
		return True
	else:
		return False
