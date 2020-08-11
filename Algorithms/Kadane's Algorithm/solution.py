def kadanesAlgorithm(arr):

    n = len(arr)
    currentSum = maxSum = arr[0]

    for i in range(1, n):

        currentSum = max(arr[i], currentSum+arr[i])
        maxSum = max(currentSum, maxSum)

    return(maxSum)

arr = list(map(int, input().split()))
print(kadanesAlgorithm(arr))
