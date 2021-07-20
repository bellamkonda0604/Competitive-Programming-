# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.

def sameSize(m1):
    k= -1
    for i in range(len(m1)):
        l = []
        l = m1[i]
        if ( k == -1):
            k = len(l)
        else:
            if(k!=len(l)):
                return -1
    return k

def fun_matrixmultiply(m1, m2):
    x = sameSize(m1)
    y = sameSize(m2)
    if(x != len(m2)):
        return None
    else:
        # result = [[0]*len(m2[0])]*len(m1)
        result = []
        for i in range(len(m1)):
            z = []
            for j in range(len(m2[0])):
                # z[j] = 0
                z.append(0)
            result.append(z)
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    result[i][j] += m1[i][k] * m2[k][j]
        return result





