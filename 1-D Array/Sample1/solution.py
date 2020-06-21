t = int(input())

for i in range(t):
    res = []
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    j = 0
    k = -1

    while(j < n/2):
        res.append(l[j])
        res.append(l[k])
        j = j + 1
        k = k - 1
    print(*res, sep = ' ')
