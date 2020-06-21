t = int(input())

for k in range(t):
    n = int(input())
    divisors = set([1])
    i = 2
    while(i*i <= n):
        if(n % i == 0):
            divisors.add(i)
            divisors.add(n//i)   
        i = i + 1
    if(sum(divisors) == n):
        print("YES")
    else:
        print("NO")
