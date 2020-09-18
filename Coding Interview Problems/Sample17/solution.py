coins = list(map(int, input().split()))
target = int(input())

n = len(coins)
res = [0]
for i in range(target):
    res.append(target+1)

for amount in range(1, target+1):
    for coin in coins:
        if(coin <= amount):
            diff = res[amount - coin]
            if(diff+1 < res[amount]):
                res[amount] = diff + 1

print(res)
print(res[target])
