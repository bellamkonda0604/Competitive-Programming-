# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	# l = []
	# if a == []:
	# 	return -1
	# for i in a:
	# 	if i < 0:
	# 		x = abs(i)
	# 		l.append(x)
	# 	else:
	# 		l.append(i)
	# a = sorted(l)
	# print(a)
	# for i in a:
	# 	diff = abs(a[1] - a[0])
	# print(diff)
	a.sort()
	diff = 0
	if(len(a) == 0):
		return -1
	smalldiff = abs(a[0] - a[1])
	for i in range(len(a)-1):
		diff = abs(a[i] - a[i+1])
		if(diff < smalldiff):
			smalldiff = diff
	return smalldiff

# print(smallestdifference([1,1,2]))