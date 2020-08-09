N = int(input())
data = []
for i in range(N):
    line = list(map(str, input().split()))
    data.append(line)
record = "Stocks not traded"
data = sorted(data)
for i in data:
    if(i[1])=='Buy':
        for j in data:
            if(j[2]==i[2] and j[1]=='Sell' and int(j[3]) < int(i[3]) and int(j[4])>0):
                if(int(i[4]) > int(j[4])):
                    i[4] = int(i[4]) - int(j[4])
                    j[4] = str(0)
                    record = ":".join([i[2],j[3]])
                if(int(i[4]) < int(j[4])):
                    i[4] = int(i[4]) - int(j[4])
                    j[4] = int(j[4]) - int(i[4])
    #del data[data == i]
    N-=1

print(record)