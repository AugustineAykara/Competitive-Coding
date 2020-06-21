def countSquares(a, b):
    minSide = min(a, b)
    maxSide = max(a, b)
    pair = (minSide, maxSide)

    if(minSide == 0):
        return(0)
    if(minSide == 1):
        return(minSide * maxSide)


    count = maxSide // minSide
    newSide = maxSide % minSide

    count += countSquares(minSide, newSide)
    dictionary[pair] = count

    return(count)

p = int(input())
q = int(input())
r = int(input())
s = int(input())

dictionary = {}
res = 0
for i in range(p, q+1):
    for j in range(r, s+1):
        res += countSquares(i, j)
print(res)
