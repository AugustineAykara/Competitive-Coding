from itertools import combinations

def solutuion(l):
    l.sort(reverse=True)
    for size in range(len(l), 0, -1):        
        for combinationList in combinations(l, size):          
            if(sum(combinationList)%3 == 0):
                return(int(''.join(map(str, combinationList))))
    return(0)

l = list(map(int, input().split()))
print(solutuion(l))
