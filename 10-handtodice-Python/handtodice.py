# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
	# your code goes here
	n = hand
	l = []
	# print(n)
	while (n > 0):
		x = n % 10
		n = n // 10
		# print(n)
		l.append(x)
		# print(l)
	return tuple(l[::-1])
	# print(l.reverse())

# print(handtodice(123))
