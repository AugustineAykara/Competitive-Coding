def zeroSumSubArray():

    dictionary = {}
    sum = 0
    for num in arr:

        sum += num
        if(sum == 0 or sum in dictionary):
            return("Subarray exist")
        dictionary[sum] = True

    return("Subarray do not exist")

arr = list(map(int, input().split()))
print(zeroSumSubArray())
