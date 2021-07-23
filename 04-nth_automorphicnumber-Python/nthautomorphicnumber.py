# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def digitcount(n):
	count = 0
	while (n>0):
		count += 1
		n = n//10
	return count

def isautomorphicnumber(n):
	if n == (n ** 2) % (10 ** digitcount(n)):
		return True
	return False


def nthautomorphicnumbers(n):
	# Your code goes here
	count = 1
	i = 0
	while count < n:
		i += 1
		if isautomorphicnumber(i):
			count += 1
	return i
