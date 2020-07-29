def getPairValues():

    dictionary = {i: False for i in arr}
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            pairSum = arr[i] + arr[j]
            if(pairSum in dictionary):
                print((arr[i], arr[j]))
                dictionary[pairSum] = True

    print(dictionary)

arr = list(map(int, input().split()))
getPairValues()
