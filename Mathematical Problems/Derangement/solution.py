def derangements(n):

    if(n == 1):
        return(0)
    if(n == 0 or n == 2):
        return(1)

    d = [0 for i in range(0, n+1)]
    d[0] = 1
    d[1] = 0
    d[2] = 1
    for i in range(3, n+1):
        d[i] = (i-1)*(d[i-1] + d[i-2])
    return(d[i])

n = int(input())
print(derangements(n))
