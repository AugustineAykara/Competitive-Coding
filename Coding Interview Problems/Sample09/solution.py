def maxLengthSubarray(arr, target):

    n = len(arr)
    dictionary = {}
    length = sum = 0

    for i in range(n):

        sum += arr[i]

        if(sum not in dictionary):
            dictionary[sum] = i

        if(sum == target):
            length = max(length, i+1)
            endIndex = i
            startIndex = endIndex - length + 1

        elif((sum-target) in dictionary and length < i-dictionary[sum-target]):

            length = i-dictionary[sum-target]
            endIndex = i
            startIndex = endIndex - length + 1

    print("length =", length)
    print("index =", (startIndex, endIndex))

arr = list(map(int, input().split()))
target = int(input())

maxLengthSubarray(arr, target)
