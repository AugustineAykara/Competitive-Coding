def getLargestSmallest(value):
    largest = 0
    smallest = 9

    while(value):
        lastDigit = value % 10
        largest = max(largest, lastDigit)
        smallest = min(smallest, lastDigit)
        value //= 10
    return(largest, smallest)


def countPairs(value):
    if(value == 2):
        return(1)
    if(value >= 3):
        return(2)
    return(0)


t = int(input())

for _ in range(t):

    n = int(input())
    numbers = list(map(int, input().split()))
    newList = []

    for value in numbers:
        largest, smallest = getLargestSmallest(value)
        temp = str(largest*11 + smallest*7)

        if(len(temp) > 2):
            temp = temp[-2:]
        newList.append(temp)

    evenList = [0] * 10
    oddList = [0] * 10
    count = 0

    for i, value in enumerate(newList):
        first = int(value[0])
        if((i+1) % 2 == 0):
            evenList[first] += 1
        else:
            oddList[first] += 1

    for i in range(10):
        count += min(2, countPairs(evenList[i]) + countPairs(oddList[i]))

    # print(newList)
    # print(evenList)
    # print(oddList)
    print(count)
