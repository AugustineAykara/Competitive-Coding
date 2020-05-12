def getDecimalToBaseValue(z, b):
    res = []
    while(z>0):
        rem = z%b
        res.append(rem)
        z = z/b
    res.reverse()
    res = map(str, res)
    res = int(''.join(res))
    return(res)

def getDecimalValue(x, b):
    res = 0
    for value, p in zip(x, range(len(x)-1, -1, -1)):
        res += int(value)*(b**p)
    return(res)

def subtract(x, y, b):
    if(b == 10):
        return(int(x)-int(y))
    else:
        x = getDecimalValue(x, b)
        y = getDecimalValue(y, b)
        res = getDecimalToBaseValue(x-y, b)
        return(res)


def solution(n, b):
    arr = []
    while(True):
        x = "".join(sorted(str(n), reverse=True))
        y = "".join(sorted(str(n)))    
        z = subtract(x, y, b)

        if(len(str(z)) != len(x)):
            z = z * pow(10 ,(len(x)-len(str(z)))) 

        for count, item in enumerate(arr):
          if item == z:            
            return(count+1)
        n, arr = z, [z] + arr

n = int(input())
b = int(input())
print(solution(n, b))
