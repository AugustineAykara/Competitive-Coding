def getPairValues():

    for num in arr:

        diff = target - num
        if (num in dictionary):
            print(dictionary[num], num)
        elif (diff not in dictionary):
            dictionary[diff] = num

target = int(input())
arr = list(map(int, input().split()))
dictionary = {}

getPairValues()
