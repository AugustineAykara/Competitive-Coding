import math
t = int(input())

for _ in range(t):
    n = int(input())
    print(int(math.log(n, 2)+1))
    
    
# OR    
    
# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     n = str(bin(n))
#     print(len(n)-2)
