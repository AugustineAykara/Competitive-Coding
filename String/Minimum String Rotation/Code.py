def minimumStringRotation(arr ,dictionary):
    stringSet = [arr[0]]
    
    for string in arr:
        if(string not in stringSet):
            return -1
        
        stringSet = []
        for rot in range(len(string)):
            if(string not in stringSet):
                stringSet.append(string);
                if string in dictionary:
                    dictionary[string] += rot
                else:
                    dictionary[string] = rot
                string = string[1:len(string)] + string[0]
                
    print(dictionary)
    resValue = min(dictionary.values())
    resKey = min(dictionary, key=dictionary.get)
    print(resKey)
    return(resValue)

n = int(input())
arr = [input() for _ in range(n)]
dictionary = {}
print(minimumStringRotation(arr, dictionary))



        
