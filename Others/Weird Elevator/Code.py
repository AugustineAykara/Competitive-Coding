import math

def isPrime(num):
    squareRoot = int(math.sqrt(num)) + 1
    for i in range(3, squareRoot, 2):
        if(num % i == 0):
            return(False)
    return(True)

primeList = []
primeList.append(2)
for i in range(3, 1000000, 2):
    if(isPrime(i)):
        primeList.append(i)

t = int(input())
for _ in range(t):
    x, y, m = map(int, input().strip(' ').split())    
    floorNumber = math.gcd(x, y)
    xPrimeFactor = x // floorNumber
    yPrimeFactor = y // floorNumber
    seconds = 0
    for i in range(0, m):
        prime = primeList[i]
        if(prime >= m):
            break
        while(xPrimeFactor % prime == 0):
            xPrimeFactor = xPrimeFactor/prime
            seconds += 1
        while(yPrimeFactor % prime == 0):
            yPrimeFactor = yPrimeFactor/prime
            seconds += 1
        if(xPrimeFactor == 1 and yPrimeFactor == 1):
            break
    if(xPrimeFactor == 1 and yPrimeFactor == 1):
        print(seconds, floorNumber)
    else:
        print(-1)
