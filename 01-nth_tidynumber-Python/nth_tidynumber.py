# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def tidyNumber(n):
    n = abs(n)
    temp = n
    x = 0
    y = 0
    while(temp > 0):
        x = temp % 10
        temp = temp // 10
        y = temp % 10
        if (x < y):
            return False
    return n

def fun_nth_tidynumber(n):
    count = 0
    i = 1
    while (count <= n):
        if (tidyNumber(i)):
            count = count + 1
        i = i + 1
    return i-1


# print(fun_nth_tidynumber(15))