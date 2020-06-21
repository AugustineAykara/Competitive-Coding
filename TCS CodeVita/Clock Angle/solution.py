rotationPeriod = int(input())
longitude = float(input())

time = (rotationPeriod * longitude) / 360

minute = time * 60  # 330 minute
hour = minute // 60
hour = hour % 12    # 5 hr
minute = minute % 60  # 30 min

# print(hour, minute)

minuteAngle = minute * 6
hourAngle = (hour * 30) + (minute*30)//60

# print(hourAngle, minuteAngle)

minAngle = abs(minuteAngle - hourAngle)

if(minAngle > 180):
    minAngle = 360 - minAngle

print("{:.2f}".format(minAngle))

