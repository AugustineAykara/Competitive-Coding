t = int(input())
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for _ in range(t):
    l, r = map(int, input().strip(' ').split())
    count = 0
    for num in range(l, r+1):
        for p in prime:
            if(1<<(p-1) & num):
                count += 1      
    print(count)
