t = int(input())

for _ in range(t):
    posList = []
    pos = 0
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    
    # to find index value of -1 in list
    while(True):
        try:
            pos = arr.index(-1, pos)
            posList.append(pos)
            pos += 1
        except ValueError as e:
            break
    
    # to find the corresponding value for -1
    for pos in posList:
        if((arr[pos-1] + arr[pos+1]) % 2 == 0):
            res = abs(arr[pos-1] - arr[pos+1])
            arr[pos] = res
        else:
            res = (arr[pos-1] + arr[pos+1]) // 2
            arr[pos] = res
            
    # subtracting by 1 except the last value
    for pos, num in enumerate(arr[0:n-1]):
        if(num == 1):
            continue
        arr[pos] = num - 1
        
    print(*arr,  sep='')
