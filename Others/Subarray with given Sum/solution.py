n = int(input())
arr = list(map(int, input().strip().split(" ")))
flag = 0
ptr1 = 0
ptr2 = 0
currentSum = arr[0]

while(ptr1 < len(arr)):
	
	if(currentSum == n):
		flag = 1
		print(arr[ptr2 : ptr1+1])
	
	if(currentSum <= n):
		ptr1 += 1
		if(ptr1 < len(arr)):
			currentSum += arr[ptr1]
	
	else:
		currentSum -= arr[ptr2]
		ptr2 += 1

if(flag == 0):
    print("No subarray with given sum exists")
