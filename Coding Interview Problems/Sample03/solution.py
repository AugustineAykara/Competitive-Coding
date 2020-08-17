def fibonacci(n):

    if (memo[n] != 0):
        return (memo[n])
    elif (n == 0):
        return (0)
    elif (n == 1 or n == 2):
        return (1)
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return (memo[n])

n = int(input())
memo = [0] * (n)
print(fibonacci(n-1))
