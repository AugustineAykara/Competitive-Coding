t = int(input())

for _ in range(t):
    string = input()
    wordList = []
    resultantList = []
    dif = 1
    i = 0
    j = 1
    
    # to break the string into words
    for k in range(1, len(string) + 1):
        word = string[i : j]
        if(word == ''):
            break
        wordList.append(word)
        dif = dif + k
        i = j
        j = dif + k
    
    # top remove last word if it is shorter than the previous word
    if(len(wordList) != 1):
        if(len(wordList[-1]) < len(wordList[-2])):
            wordList.pop()
        
    # to perform the given operation on word
    for word in wordList:
        if(len(word) > 2):
            resultantWord = word[0] + word[-1]
            resultantList.append(resultantWord)
        else:
            resultantList.append(word)
            
    print(*resultantList, sep='')
