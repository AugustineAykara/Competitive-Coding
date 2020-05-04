n = int((input()))
arr = list(map(int, input().split()))
arr = sorted(arr, reverse=True)
avg = sum(arr)//2
bob = []
for num in arr:
    bob.append(num)
    if(sum(bob) > avg):
        print(len(bob))
        break
