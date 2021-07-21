# Background: we can represent a polynomial as a list of its coefficients. For example, [2, 3, 0, 4] could represent 
# the polynomial 2x3 + 3x2 + 4. With this in mind, write the function multiplyPolynomials(p1, p2) which takes two 
# lists representing polynomials as just described, and returns a third list representing the polynomial which is 
# the product of the two. For example, multiplyPolynomials([2,0,3], [4,5]) represents the problem (2x**2 + 3)(4x + 
# 5), and:    (2x**2 + 3)(4x + 5) = 8x**3 + 10x**2 + 12x + 15
# And so this returns the list [8, 10, 12, 15].

def multipolynomials(p1, p2):
	# Your code goes here
	m = len(p1)
	n = len(p2)
	l = [0] * (m + n - 1)
	# print(l)
	for i in range(m):
		for j in range (n):
			# if p1[i] != 0 and p2[j] != 0:
			l[i + j] += p1[i] * p2[j]
	return l

# print(multipolynomials([1, -1], [1, -1]))