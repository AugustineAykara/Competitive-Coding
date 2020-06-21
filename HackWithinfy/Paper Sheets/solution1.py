h, w = map(int, input("Enter initial dimension : ").strip().split(" "))
h1, w1 = map(int, input("Enter new dimension : ").strip().split(" "))
count = 0

while(h > h1):
    if(h&1 == 1):   #if h is odd
        h = h >> 1  #divides h by 2
        h += 1
    else:           #if h is even
        h = h >> 1
    count += 1
    
while(w > w1):
    if(w&1 == 1):   #if w is odd
        w = w >> 1  #divides w by 2
        w += 1
    else:           #if w is even
        w = w >> 1
    count += 1
    
print(count)
