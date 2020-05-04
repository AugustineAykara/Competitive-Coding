from functools import reduce
n = int(input())

for i in range(n):
    arr = list(map(int,input().split()))
    n = arr[0]
    arr = arr[1:]
    res = reduce(lambda x,y : x|y, arr)
    print(res)
   
    temp = 0
    bitWiseOR = 0
    count = 1
    arr.sort(reverse = True)
    
    for k in range(0, n):
        bitWiseOR = temp | arr[k]
        if bitWiseOR == res:
            print(count)
            break
        elif(temp != bitWiseOR):
            count += 1
            temp = bitWiseOR
