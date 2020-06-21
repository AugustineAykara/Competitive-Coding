class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {"{" : "}", "(" : ")", "[" : "]"}
        stack = []
        for i in range(len(s)):
            if(s[i] in bracket):
                stack.append(s[i])
            else:
                if(stack == []):
                    return(False)                    
                if(s[i] == bracket[stack[-1]]):
                    stack.pop()
                else:
                    return(False)
        if(stack == []):
            return(True)
        else:
            return(False)
