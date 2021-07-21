# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isprime(n):
	if n < 2:
		return False
	for i in range(2,n):
		if n % i == 0:
			return False
	return True

def squareofdigits(n):
	res = 0
	while (n > 0):
		res += (n % 10)**2
		n = n//10
	return res

def ishappy(n):
	while 1:
		if n == 1:
			return True
		elif n == 4:
			return False
		else:
			n = squareofdigits(n) 
	return False

def fun_nth_happy_prime(n):
	count  = -1
	i = 2
	while True:
		if isprime(i) and ishappy(i):
			count += 1
		if count == n:
			break
		i += 1
	return i