amount = int(input())
coin = list(map(int, input().split()))

minCoin = [amount+1 for i in range(amount+1)]
minCoin[0] = 0

for i in range(1, amount+1):
    for j in coin:
        if(i >= j):
            minCoin[i] = min(minCoin[i-j]+1, minCoin[i])

if(minCoin[amount] == amount+1):
    print(-1)
else:
    print(minCoin[amount])
