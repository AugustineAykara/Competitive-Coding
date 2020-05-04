fileOutput = open("output_e_also_big.in", "w")

with open('e_also_big.in') as fileInput:
    maxSlice, pizzaTypes = [int(x) for x in next(fileInput).split()]
    sliceList = []
    for line in fileInput:
        sliceList.append([int(x) for x in line.split()])
    
listLength = len(sliceList[0])
count = 0
pos = []

for slice in reversed(sliceList[0]):
    if(slice <= maxSlice):
        pos.append(listLength-1)
        count += 1
        maxSlice -= slice
    listLength -= 1

print(count)
print(' '.join(map(str, sorted(pos))))
fileOutput.write(str(count) + "\n")
fileOutput.writelines(' '.join(map(str, sorted(pos))))

fileInput.close()
fileOutput.close()