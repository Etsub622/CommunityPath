class Solution:
    def minimumSteps(self, s: str) -> int:
        lst=''
        c_0=s.count('0')
        c_1=s.count('1')
        lst+=(c_0*'0')
        lst+=(c_1*'1')
        
        l=0
        count=0
        for i in range(len(lst)):
            if s[i]=='0':
                count+=i-l
                l+=1
        return count       

        