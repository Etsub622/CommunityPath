class Solution:
    def romanToInt(self, s: str) -> int:
        sum=0
        dic={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000}

        for i in range(len(s)):
            sum+=dic[s[i]]
            if i ==0:
                continue
            if s[i]=='V' or s[i]=='X':
                if s[i-1]=='I':
                    sum-=2*(dic['I'])
                 
            if s[i]=='L' or s[i]=='C':
                if s[i-1]=='X':
                    sum-=2*(dic['X'])
                  

            if s[i]=='D' or s[i]=='M':
                if s[i-1]=='C':
                    sum-=2*(dic['C'])
                                     
                

        return sum