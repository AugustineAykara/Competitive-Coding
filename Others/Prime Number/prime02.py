l, r = map(int, input().split())
  
for num in range(l, r+1): 
      
   if num > 1: 
       for n in range(2, num//2 + 1): 
           if (num % n) == 0: 
               break
       else: 
           print(num, end=' ') 
