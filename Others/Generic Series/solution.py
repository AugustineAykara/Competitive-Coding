t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())
    if(a == 0 and b == 0):
        print(0)
    elif(n == 0):
        print(a)
    elif(n == 1):
        print(b)
    else:
        while(n-2 >= 0):
            c = a + b
            a = b
            b = c
            n -= 1
        print(c)
