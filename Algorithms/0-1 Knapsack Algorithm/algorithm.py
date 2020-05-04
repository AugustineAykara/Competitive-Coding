# 0/1 Knapsack Problem

m = int(input(" Enter knapsack capacity : "))   #maxCapacity
p = list(map(int, input(" Enter profit value of each object : ").split()))     #profit
w = list(map(int, input(" Enter weight value of each object : ").split()))     #weight

table = [[0 for x in range(m+1)] for y in range(len(w)+1)]

for item in range(1, len(w)+1):
  for value in range(m+1):    
    if(w[item-1] <= value):
      table[item][value] = max(table[item-1][value], table[item-1][value-w[item-1]] + p[item-1])
    else:
      table[item][value] = table[item-1][value]  
    
print(table[item][value])
