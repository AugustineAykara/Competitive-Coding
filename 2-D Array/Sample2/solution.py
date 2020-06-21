t = int(input())

for _ in range(t):
    
    n, m = map(int, input().split())
    matrix=[] 
    for i in range(n):
        rowValue = input().split()
        matrix.append(rowValue)
        
    
    (i, j, count1) = (0, 0, 0)
    while(i != n-1 or j != n-1):
 
        if(i == j and matrix[i+1][j+1] == '0'):
            (i, j) = (i+1, j+1)
                    
        elif(i != n-1 and matrix[i+1][j] == '0'):        
            i += 1
                
        else:
            j += 1
        count1 += 1
        
    (i, j, count2) = (0, 0, 0) 
    while(i != n-1 or j != n-1):
   
        if(i == j and matrix[i+1][j+1] == '0'):
            (i, j) = (i+1, j+1)
                    
        elif(j != n-1 and matrix[i][j+1] == '0'):        
            j += 1
                
        else:
            i += 1
        count2 += 1
        
    print(min(count1,count2))
