# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.


from types import resolve_bases


def fun_recursions_alternatingsum(l):
	if l != 0:
		even = sum(l[::2])

		odd = sum(l[1::2]) 

		result = even - odd
	return result