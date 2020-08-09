enemies = int(input())
pList = list(map(int, input().split()))
kitty = 0
idx = 1
def selectOpponent(pList):
    if(len(pList)==3):
        return 1
    elif(len(pList)==2):
        if(pList[0]<pList[1]):
            return 0
        else:
            return 1
    elif(len(pList)==1):
        return 0
    elif(len(pList)==4):
        max_idx = 1
        for i in range(2,(len(pList)-1)):
            if(pList[i]>pList[max_idx]):
                max_idx = i
        return max_idx
    elif(len(pList)>4):
        min_idx = 1
        for i in range(2,(len(pList)-1)):
            if(pList[i]<pList[min_idx]):
                min_idx = i
        return min_idx
while(len(pList)>=1):
    idx = selectOpponent(pList)
    if(len(pList)==1):
        kitty+= pList[idx]
    elif(len(pList)==2):
        if(idx==0):
            kitty+= pList[idx]*pList[idx+1]
        else:
            kitty+= pList[idx]*pList[idx-1]
    elif(len(pList)>=3):
        if(pList[idx-1]>pList[idx+1]):
            kitty+= pList[idx]*pList[idx-1]+pList[idx+1]
        else:
            kitty+= pList[idx]*pList[idx+1]+pList[idx-1]
    del pList[idx]
print(kitty)