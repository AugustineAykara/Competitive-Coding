arr = list(map(int, input().split()))
resCount = 0
for i in range(32):
    count = 0
    for j in range(len(arr)):
        if(arr[j] % 2 == 1):
            count += 1
        arr[j] >>= 1
    resCount += 2*count*(len(arr)-count)
print(resCount)   
