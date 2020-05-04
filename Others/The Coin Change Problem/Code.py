n, m = map(int, input().strip().split(" "))
c = list(map(int, input().split()))

table = [[0 for x in range(n+1)] for y in range(len(c)+1)]
table[0][0] = 1


for row in range(1, len(c)+1):
    for col in range(n+1):
        if(col < c[row-1]):
            table[row][col] = table[row-1][col]
        else:
            table[row][col] = table[row-1][col] + table[row][col - c[row-1]]

print(table[row][col])
