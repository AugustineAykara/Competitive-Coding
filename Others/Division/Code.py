t = int(input())

for _ in range(t):
    a, b, c = map(int, input().strip(' ').split())
    remainder = c % a
    
    if(a >= b):
        if(remainder > b):
            res = c - (remainder-b)
        elif(remainder < b):
            res = (c-remainder)  - (a-b)
        else: 
            res = c
        print(res)
        
    else:
        print(-1)
