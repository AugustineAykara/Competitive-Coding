def getResult(arr, b):
	arr.sort()
	maxSum = 0
	count = 0
	for value in arr:

		maxSum += value
		count += 1
		if (maxSum > b):
			return (count - 1)

	return (count)

n, b = list(map(int, input().split()))
arr = list(map(int, input().split()))
print(getResult(arr, b))
