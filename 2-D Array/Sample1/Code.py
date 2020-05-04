# created a dictionary for alphabets
alphabets = 'abcdefghijklmnopqrstuvwxyz'
dictionary = {}
for i, letter in zip(range(1, len(alphabets)+1),alphabets):
    dictionary[i] = letter
    
t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[2:]
    arrList = []
    matrix = []
    
    # to form elements in list in list form (2D array)
    for i in range(0, n*n, n):
        for j in range(n):
            arrList.append(arr[i+j])
        matrix.append(arrList)
        arrList = []
    
    # to get the element in generator highlighted postion
    k = 0
    for i in range(n-1, 0, -2):
        value = matrix[i][k]
        arrList.append(value)
        k += 1

    for i in range(0, n, 2):
        value = matrix[i][k]
        arrList.append(value)
        k += 1
        
    # to get the corresponding alphabet
    for element in arrList:
        print(dictionary[element%26], end='')
    print()
