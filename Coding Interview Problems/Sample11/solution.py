def sortYArray(y, ny):

    j = 1
    while(j < ny and y[j-1] > y[j]):
        y[j-1], y[j] = y[j], y[j-1]
        j += 1
    return(y)

x = list(map(int, input().split()))
y = list(map(int, input().split()))

nx = len(x)
ny = len(y)

i = 0
while(i < nx):

    if(x[i] > y[0]):
        x[i], y[0] = y[0], x[i]
        y = sortYArray(y, ny)

    i += 1

print("X =", x)
print("Y =", y)
