def derangement(n):

    if (n == 1):
        return (0)
    if (n == 0 or n == 2):
        return (1)

    # using memoization
    d = [0 for i in range(0, n + 1)]
    d[0] = 1
    d[1] = 0
    d[2] = 1

    for i in range(3, n + 1):
        d[i] = (i - 1) * (d[i - 1] + d[i - 2])
    return (d[i])

    # or (using recursion)
    # result = (n - 1) * (derangement(n-1) + derangement(n-2))
    # return(result)

n = int(input())
result = derangement(n)
print(result)
