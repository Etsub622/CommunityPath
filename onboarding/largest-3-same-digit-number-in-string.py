class Solution:
    def largestGoodInteger(self, num: str) -> str:
        output=''
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]: 
                output=max(output,num[i:i+3])
        
        return output            
        