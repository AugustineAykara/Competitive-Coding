arr = list(map(int, input().split()))
xor = 0

for value in arr:
    xor = xor ^ value

print(xor)
