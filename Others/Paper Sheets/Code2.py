import math

h, w = map(int, input("Enter initial dimension : ").strip().split(" "))
h1, w1 = map(int, input("Enter new dimension : ").strip().split(" "))

count = math.ceil(math.log(h,2) - math.log(h1,2))           #returns how many time h can be divide by 2 to get h1
count = count + math.ceil(math.log(w,2) - math.log(w1,2))   #returns how many time w can be divide by 2 to get 21

print(count)
