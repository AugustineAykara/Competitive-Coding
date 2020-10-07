def fib(n):
    
    if(n in memo):
        return(memo[n]) 
   
    if(n == 1 or n == 0):
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

n = int(input())
memo = {0:0, 1:1}
print(fib(n-1))
