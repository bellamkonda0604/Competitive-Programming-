# isPalindromicPrime() Write a function isPalindromicPrime that takes a value n as a parameter and returns True if the given n is a palindrome and prime and False otherwise.
# assert (isPalindromicPrime(2) == True)
# assert (isPalindromicPrime(10) == False)
# assert (isPalindromicPrime(104) == False)
# assert (isPalindromicPrime(235) == False)
# assert (isPalindromicPrime(131) == True)
# assert (isPalindromicPrime(900) == False)
# assert (isPalindromicPrime(101) == True)
# assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
# assert (isPalindromicPrime(121) == False)
# print("All test cases passed... :-)")

def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def ispalindrome(n):
    temp = n
    rev = 0
    while(n > 0):
        d = n % 10
        rev = rev * 10 + d
        n = n // 10
    if(temp == rev):
        return True
    else:
        return False

def ispalindromeprime(n):
    if isprime(n) and ispalindrome(n):
        return True
    return False
