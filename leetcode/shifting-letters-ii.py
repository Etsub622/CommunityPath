class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n=len(s)
        diff=[0]*(n+1)
        
        for l,r,k in shifts:
            if k==1:
                diff[l]+=k
                diff[r+1]-=k 
            else:
                diff[l]-=1
                diff[r+1]+=1   

        acc=0
        output=[0]*n
        for i in range(len(diff)-1):
            acc+=diff[i]
            output[i]=acc

        l=0
        shifted = ""
        for char in s:
            shifted_char = chr(((ord(char) - ord('a') + output[l]) % 26) + ord('a'))
            shifted += shifted_char
            l+=1

        return shifted    
