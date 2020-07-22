arr = list(map(int, input().split()))

first = arr[0]
second = arr[1]
third = arr[2]

if(first > second):
    first, second = second, first

if(first > third):
    first, third = third, first

if(second > third):
    second, third = third, second

print(first, second, third)

for i in range(3, len(arr)):
    if(arr[i] < third):
        third = arr[i]
        if(third < second):
            second, third = third, second
            if(second < first):
                first, second = second, first

    print(first, second, third)

print(third)
