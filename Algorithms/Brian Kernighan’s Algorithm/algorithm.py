def setBitCount(n):
    if(n == 0):
        return(0)
    else:
        return(1 + setBitCount(n & (n-1)))

n = int(input())
print("Binary representation : " + format(n, 'b'))
print("Number of set bit :", setBitCount(n))
