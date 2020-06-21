class Solution:
    def reverse(self, num: int) -> int:
        rev = 0
        flag = 0
        if(num < 0):
            flag = 1
            num *= -1
        while(num > 0):
            last = num%10
            rev = rev*10 + last
            num = num//10
        if(rev < -2**31 or rev > 2**31-1):
            return(0)
        if(flag == 0):
            return(rev)
        else:
            return(rev*-1)
