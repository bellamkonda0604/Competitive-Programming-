# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def digitCount(x):
	count = 0
	while (x > 0):
		count += 1
		x = x // 10
	return count

def rotate(x):
	y = x
	n = y % 10
	y = y // 10
	count = 0
	temp = x
	while (temp > 0):
		temp = temp // 10
		count += 1
	x = y + n * 10 ** (count-1)
	return x

def isPrime(x):
	if (x < 2):
		return False
	for i in range(2,x):
		if (x % i == 0):
			return False
	return True

def isCircular(x):
	len = digitCount(x)
	if(len == 1):
		return True
	else:
		cnt = 0
		while cnt < len:
			if(not isPrime(x)):
				return False
			x = rotate(x)
			cnt += 1
			if cnt == len:
				return True
	return False

def nthcircularprime(n):
	# Your code goes here
	i = 2
	count = 0
	while(count < n):
		if(isPrime(i) and isCircular(i)):
			count += 1
		i += 1
	return i-1