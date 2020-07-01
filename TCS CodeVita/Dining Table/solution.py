factorailTable = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]

def ncr(n, r):
    if(n == r or r == 0):
        return(1)
    if(r == 1):
        return(n)
    result = factorailTable[n]//factorailTable[r]
    result = result // factorailTable[n-r]
    return(result)

r, n = list(map(int, input().split()))
peoplePerTable = n // r
extra = n % r

table = [peoplePerTable for _ in range(r)]
result = 1

for i in range(extra):
    table[i] += 1

for people in table:
    result *= ncr(n, people)
    n -= people

print(result)
