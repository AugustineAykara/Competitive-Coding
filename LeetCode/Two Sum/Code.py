class Solution:
    def twoSum(self, l, target: int):
        dictionary = {}
        for i, num in zip(range(len(l)), l):
            dif = target - num
            if(dif not in dictionary):
                dictionary[num] = i
            else:
                return (dictionary[dif],i)
            
