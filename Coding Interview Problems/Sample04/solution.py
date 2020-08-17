def getPairValues():

    dictionary = {}
    for num in arr:

        if (num in dictionary):
            print(dictionary[num], num)

        diff = target - num
        dictionary[diff] = num

target = int(input())
arr = list(map(int, input().split()))
getPairValues()
