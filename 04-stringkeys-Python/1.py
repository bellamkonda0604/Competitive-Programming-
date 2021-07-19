def hasConsecutivedigits(n):
    n = abs(n)
    flag = False
    previousDigit = -1
    while n > 0:
        lastDigit = n % 10
        n = n // 10
        if lastDigit == previousDigit - 1:
            flag = True
            print(lastDigit,previousDigit)
            # return True
        # if lastDigit != previousDigit:
        #     print(lastDigit, previousDigit)
        previousDigit = lastDigit
    return flag
print(hasConsecutivedigits(2201523))