def checkConsecutiveSubarray(arr, minValue, maxValue):

    if(maxValue-minValue != len(arr)-1):
        return(False)

    dictionary = {k : False for k in arr}

    for k in arr:
        if(dictionary[k]):
            return(False)
        dictionary[k] = True

    return(True)


arr = list(map(int, input().split()))
n = len(arr)
length = startIndex = endIndex = 0

for i in range(n):
    minValue = arr[i]
    maxValue = arr[i]

    for j in range(i+1, n):
        minValue = min(minValue, arr[j])
        maxValue = max(maxValue, arr[j])

        if (checkConsecutiveSubarray(arr[i:j+1], minValue, maxValue)):
            if(length < maxValue - minValue + 1):                           # or if(length < len(arr[i:j+1])

                length = maxValue - minValue + 1
                startIndex = i
                endIndex = j

print("Index =", (startIndex, endIndex))
print("Sub-Array =", arr[startIndex : endIndex+1])
