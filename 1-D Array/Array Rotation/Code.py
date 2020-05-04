t = int(input())

for i in range(t):
    n, k = map(int, input().strip().split(' '))
    arr = list(map(int, input().split()))    
    for j in range(k):
        arr = arr[-1:] + arr[:-1]
      
    print(*arr, sep = " ")
