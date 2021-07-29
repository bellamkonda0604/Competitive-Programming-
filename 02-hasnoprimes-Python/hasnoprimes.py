# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def isprime(n):
	if n < 2:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def fun_hasnoprimes(l):
	for row in l:
		for col in row:
			if(isprime(col)):
				return False
	return True

# print(fun_hasnoprimes([2]))

