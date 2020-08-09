read_input = list(map(int, input().split()))
D = int(read_input[0])
p = int(read_input[1])
hpp = D//p
pList = list()
count = 0
hour = 2

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True

for hour in range(2,hpp):
    if(is_prime(hour)):
        pList = list()
        pList.append(hour)
        for i in range(1,p):
            if(is_prime(hour+(hpp*i))):
                pList.append(hour)
                if(len(pList)==p):
                    count+=1
print(count)