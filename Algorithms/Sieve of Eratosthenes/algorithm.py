def sieveEratosthenes(n):
	arr = [True for i in range(n+1)]
	arr[0] = arr[1] = False
	p = 2

	while(p*p <= n):
		if(arr[p] == True):
			for i in range(p*2, n+1, p):
				arr[i] = False
		p += 1

	for i in range(n+1):
		if(arr[i]):
			print(i, end=" ")

n = int(input())
sieveEratosthenes(n)
