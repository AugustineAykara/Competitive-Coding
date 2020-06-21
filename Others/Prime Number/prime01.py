# Prime numbers between a range using Sieve Eratosthenes method

l, r = map(int, input().split())
if(l in [0, 1]):
    l = 2
prime = [i for i in range(l, r+1)]

num = 2
while(num**2 <= r):
    for i in range(num**2, r+1, num):
        if(i in prime):
            prime.remove(i)
    num += 1

print(*prime, sep=', ')
