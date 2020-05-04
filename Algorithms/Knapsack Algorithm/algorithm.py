# knapsack algorithm when greedy about both profit and weight

m = int(input(" Enter knapsack capacity : "))   #maxCapacity
p = list(map(int, input(" Enter profit value of each object : ").split()))     #profit
w = list(map(int, input(" Enter weight value of each object : ").split()))     #weight
pw = [a/b for a,b in zip(p, w)]     #profit/weight
n = len(pw)     #size of pw i.e. number of objects
res = 0
p = [x for _,x in sorted(zip(pw, p), reverse=True)]
w = [x for _,x in sorted(zip(pw, w), reverse=True)]
pw.sort(reverse=True)
print(" profit/weight -> ", pw)
print(" profit -> ", p)
print(" weight -> ", w)

for value, i in zip(pw, range(n)):
    if(w[i] <= m):
        m = m - w[i]
        res = res + p[i]
    else:
        res = res + p[i]*(m/w[i])
        break
    
print(res)
