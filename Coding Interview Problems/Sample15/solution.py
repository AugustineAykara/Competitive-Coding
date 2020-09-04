number = input()
n = len(number)
midIndex = n//2

if(len(number) % 2 == 1):
    mid = number[midIndex]
else:
    mid = ''

left = number[:midIndex]
right = left[::-1]

palindrome = left + mid + right

if(palindrome > number):
    print(palindrome)
else:
    if(number == n*'9'):                    # if all digits are 9
        palindrome = '1' +  (n-1)*'0' + '1'

    elif(mid):                              # if length of number odd

        if(int(mid) < 9):
            mid = str( int(mid)+1 )
            palindrome = left + mid + right
        else:
            mid = '0'
            left = str(int(left) + 1)
            right = left[::-1]
            palindrome = left + mid + right

    else:                                   # if length of number is even
        while(int(palindrome) <= int(number)):
            left = str(int(left) + 1)
            right = left[::-1]
            palindrome = left + mid + right

    print(palindrome)
