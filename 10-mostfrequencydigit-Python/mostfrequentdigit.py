# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	n = abs(n)
	max = -1
	maxCount = -1
	if (n == 0):
		return 0
	while(n > 0):
		temp = n
		Digit = n % 10
		count = 0
		while temp > 0:
			LastDigit = temp % 10
			if ( LastDigit == Digit):
				count = count + 1
			temp = temp // 10
		if( max < count):
			max = count
			maxCount = Digit
		if (max == count):
			if(Digit < maxCount):
				maxCount = Digit
		n = n // 10
	return maxCount