arr = list(map(int, input().split()))
n = len(arr)
dictionary = {}
sum = maxLength = 0
endIndex = -1

for i in range(n):

    if(arr[i] == 0):
        sum += -1
    else:
        sum += 1

    if(sum == 0):
        maxLength = i + 1
        startIndex = i - maxLength + 1
        endIndex = i

    if(sum in dictionary):
        if(maxLength < (i-dictionary[sum])):
            maxLength = i - dictionary[sum]
            startIndex = i - maxLength + 1
            endIndex = i
    else:
        dictionary[sum] = i

if(endIndex == -1):
    print("No subarray found")
else:
    print((startIndex, endIndex), " => ", arr[startIndex:endIndex+1])
