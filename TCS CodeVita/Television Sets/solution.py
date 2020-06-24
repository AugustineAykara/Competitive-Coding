def calculateRevenue(tvCount, r1, r2, n):
        totalRevenue = 0
        normalRoom = n - tvCount
        for patients in range(52):
         
            if(patients <= normalRoom):
                perDayRevenue = patients * r2
            elif(patients <= n):
                perDayRevenue = normalRoom * r2 + (patients - normalRoom) * r1
            else:
                perDayRevenue = normalRoom * r2 + tvCount * r1
           
            perDayRevenue = perDayRevenue * dictionary[patients]
            totalRevenue += perDayRevenue

        return(totalRevenue)


n = int(input())
r1, r2 = list(map(int, input().split()))
targetRevenue = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
patientCountPerDay = [0]*365
dictionary = {}
index = 0

for m in range(1, 13):
    daysLimit = days[m-1]
    for d in range(1, daysLimit+1):
        res = (6 - m) ** 2 + abs(d - 15)
        if(res not in dictionary):
            dictionary[res] = 1
        else:
            dictionary[res] += 1

for tvCount in range(n):
    currentRevenue = calculateRevenue(tvCount, r1, r2, n)
    if(currentRevenue >= targetRevenue):
        break

if(currentRevenue >= targetRevenue):
    print(tvCount)
else:
    print(n)
