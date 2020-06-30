primeUpTo100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def generateFibonacci(first, second, size):
    if(size == 1):
        return(first)
    if(size == 2):
        return(second)
    for i in range(3, size+1):
        result = first + second
        first = second
        second = result

    return(result)

def isPrime(value):
    if(value%2 == 0):
        return(False)
    i = 2
    while(i*i <= value):
        if(value % i == 0):
            return(False)
        i += 1
    return(True)


def getCombination(primeList):
    combinationList = []

    for i in primeList:
        for j in primeList:
            if(i != j):
                combination = int(str(i) + str(j))
                if(isPrime(combination)):
                    combinationList.append(combination)

    combinationList = set(combinationList)
    return(combinationList)


def getPrime():
    start = 0
    end = len(primeUpTo100) - 1

    while(start <= end and primeUpTo100[start] < n1):
        start += 1
    while(end >= start and primeUpTo100[end] > n2):
        end -= 1

    return(primeUpTo100[start : end+1])


t = int(input())
for _ in range(t):
    n1, n2 = list(map(int, input().split()))
    primeList = getPrime()
    primeCombinationList = getCombination(primeList)

    size = len(primeCombinationList)
    smallest = min(primeCombinationList)
    largest = max(primeCombinationList)

    result = generateFibonacci(smallest, largest, size)

    print(result)
