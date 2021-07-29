# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	count = 0
	l = []
	for i in range(len(L)):
		l += L[i]
	for i in range(len(l)):
		count = l.count(l[i])
		if(count > 1):
			return True
	return False