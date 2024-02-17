class Solution:
    def longestPalindrome(self, s: str) -> int:
        pali=defaultdict(int)
        for i in s:
            pali[i]+=1
        print(pali)    
        ans=0 
        single=single1=0   
        for char in pali:
            if pali[char]%2==0:
                ans+=pali[char]
            elif pali[char]>1 and pali[char]%2!=0:
                ans+=pali[char]-1
                single1+=1
            else:
                single+= pali[char]        

        return ans+1 if single!=0 or single1!=0 else ans                
        