def fib(n, memo):
    
    if(n in memo):
        return(memo[n])
    
    if(n<=1):
        return(n)
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return(memo[n])

n = int(input())
memo = {0:1, 1:1, 2:2}
print(fib(n, memo))
