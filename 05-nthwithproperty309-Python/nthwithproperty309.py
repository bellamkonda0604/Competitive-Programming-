# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
import re

def digits(n):
	return len(set("".join(re.findall(r'([\d])', str(n))))) == 10

def withproperty309(n):
	n = n ** 5
	# if len(set("".join(re.findall(r'([\d])', str(n))))) == 10:
	# 	return True
	# return False
	if digits(n):
		return True
	return False

def nthwithproperty309(n):
	# Your code goes here
	count = 0
	i = 0
	while count <= n:
		i += 1
		if withproperty309(i):
			count += 1
	return i

# print(nthwithproperty309(0))