n = int(input())
bottle = list(map(int, input().split()))

dictionary = {}
maxFrequency = -1

for value in bottle:
    if(value in dictionary):
        dictionary[value] += 1
    else:
        dictionary[value] = 1
        
    maxFrequency = max(maxFrequency, dictionary[value])

print(maxFrequency)
