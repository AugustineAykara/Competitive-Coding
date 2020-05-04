class Solution:
    def isPalindrome(self, n: int) -> bool:
        temp = n
        if(n<0):
          return(False)
        rev = 0
        while(n > 0):
          last = n%10
          rev = rev*10 + last
          n = n//10
        if(rev == temp):
          return(True)
        else:
          return(False)
