n = int(input())
bride = input()
groom = input()
result = n

m = groom.count('m')
r = groom.count('r')

for brideDrink in bride:

    if (brideDrink == 'm'):
        drink = m
        m -= 1
    else:
        drink = r
        r -= 1

    if (drink == 0):
        break;
    else:
        result -= 1

print(result)
