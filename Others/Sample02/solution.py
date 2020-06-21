t = int(input())

for _ in range(t):
   
    n = int(input())				// array size
    arr = list(map(int, input().split())) 	// array elements
    m = int(input())				// given input number
    
    remainders = {}
    
    for num in arr:
        currentRemainder = num % m
        if currentRemainder in remainders:
            remainders[currentRemainder] += 1
        else:
            remainders[currentRemainder] = 1
            
    totalPairs = 0
    for rem in remainders:
        pairs = 0
        complement = m - rem
        if(complement == m or (2*complement == m)):
            pairs = (remainders[rem] * (remainders[rem] - 1)) // 2
        elif complement in remainders:
            pairs = remainders[rem] * remainders[complement]
            remainders[rem] = 0
        totalPairs = pairs + totalPairs
        
    print(totalPairs)
