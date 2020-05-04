class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ''
        if(len(strs) == 0):
            return(longestPrefix)
        for i in range(len(min(strs))):
            temp = strs[0][i]
            for j in range(len(strs)):
                if(strs[j][i] != temp):
                    return(longestPrefix)
            longestPrefix += temp
        return(longestPrefix)
