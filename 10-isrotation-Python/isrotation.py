# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.


def len(n):
	count = 0
	while (n > 0):
		n = n // 10
		count += 1
	return count

# def rotateRight(s):
# 	return s[len(s)-1:] + s[:len(s)-1]

def isrotation(x, y):
	# Your code goes here
	if len(x) != len(y):
		return False
	# for i in range(len(x)):
	# 	x = rotateRight(x)
	# 	if(x == y):
	# 		return True
	# return False
	

	