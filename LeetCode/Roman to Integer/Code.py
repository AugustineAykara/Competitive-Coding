class Solution:

    def getValue(self, roman, l):
        if(roman == 'I'):
            l.append(1)
        elif(roman == 'V'):
            l.append(5)  
        elif(roman == 'X'):
            l.append(10)
        elif(roman == 'L'):
            l.append(50)
        elif(roman == 'C'):
            l.append(100)
        elif(roman == 'D'):
            l.append(500)
        elif(roman == 'M'):
            l.append(1000)

    def romanToInt(self, s: str) -> int:
        l = []
        for i in s:
            self.getValue(i, l)

        sum = l[-1]
        j = len(l) - 2

        while(j >= 0):
            if(l[j] >= l[j+1]):
                sum += l[j]
            else:
                sum -= l[j]
            j -= 1
        return(sum)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
