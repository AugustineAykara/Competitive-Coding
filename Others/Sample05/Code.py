t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    size = arr[0]
    arr = sorted(arr[1:], reverse = True)
    f = int(input())
    k = int(input())
    r=[]
    
    def a(f, arr, k):
        
        if(len(arr) == 0):
            return False    
        while(arr[0] > f or arr[0] > k):
            arr.remove(arr[0])
            if(len(arr) == 0):
                return False    
        if(arr[0] == f and arr[0] < k):
            r.append(arr[0])
            return True
        if(len(arr) == 1):
            return False
        for i in arr:
            if(a(f-i, arr[arr.index(i)+1:], k)):
                r.append(i)    
                return True
        return False
        
    if(a(f, arr, k)):
        print("Yes")
    else:
        print("No")
