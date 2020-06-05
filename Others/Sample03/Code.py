t = int(input())

for _ in range(t):
    shape = input()
    a = int(input())
    b = int(input())
    
    if(shape == 'rectangle'):
        area = a * b
        print(area)
    elif(shape == 'square'):
        area = (a * b)//2
        print(area)
    elif(shape == 'triangle'):
        area = a * b
        print(area)
    else:
        print('0')
    
