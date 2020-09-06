with open('input/input00.txt') as inputFile:
    l = list(map(int,inputFile.split()))
nList = []
finalList = []
for i in range(len(l)):
    temp = l[i][(len(l[i])-10):]
    nList.append(temp)
for i in range(len(l)):
    min_idx = i
    for j in range(i+1,len(l)):
        if(nList[min_idx]>nList[j]):
            min_idx = j
    nList[i], nList[min_idx] = nList[min_idx], nList[i]
for i in range(len(l)):
    temp = '+91 '+nList[i][0:5]+' '+nList[i][5:10]
    print(temp)