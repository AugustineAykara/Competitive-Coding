def getSublist(arr, target):

    dict = {0:-1}
    sum = 0

    for i in range(len(arr)):

        sum += arr[i]
        if(sum - target) in dict:
            print("Sublist found at", (dict[sum - target] + 1, i))
            
        dict[sum] = i

arr = list(map(int, input().split()))
target = int(input())
getSublist(arr, target)
