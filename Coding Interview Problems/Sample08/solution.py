def getLengthOfSubsequence(arr, n):

    dictionary = {i : 1 for i in arr}

    for i in arr[1:n]:
        for j in arr[0:i]:

            if(i > j and dictionary[i] < dictionary[j]+1):
                dictionary[i] += 1

    print(max(dictionary.values()))


arr = list(map(int, input().split()))
n = len(arr)

getLengthOfSubsequence(arr, n)
