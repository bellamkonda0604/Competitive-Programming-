# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 


# def pow3ton(n, i):
# 	if n < i:
# 		return None
# 	elif( 3 ** i <= n):
# 		return [3**i] + pow3ton(n, i+1)
# 	else:
# 		return None

def recursion_powersof3ton(n):
	# Your code goes here
	if(n <= 0):
		return []
	elif(n == 1):
		return [int(n)]
	else:
		return pow3ton(n, i = 0)


def pow3ton(n, i):
	if n < i:
		return []
	elif( 3 ** i <= n):
		return [3**i] + pow3ton(n, i+1)
	else:
		return []