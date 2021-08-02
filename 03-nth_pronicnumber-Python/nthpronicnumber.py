# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).



def pronic(n):
	x = 0
	while (x <= n) :
		if (n == x * (x + 1)):
			return True
		x += 1
	return False

def nthpronicnumber(n):
	# Your code goes here
	count = 1
	i = 0
	while(count <= n):
		i += 1
		if(pronic(i)):
			count += 1
	return i