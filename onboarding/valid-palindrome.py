class Solution:
    def isPalindrome(self, s: str) -> bool:
        output=''
        for i in s:
            if i.isalnum():
                output+=i.lower()
              
        l,r=0,len(output)-1 
        while l<r:
            if output[l]!=output[r]:
                return False
            l+=1
            r-=1  
        return True            

         
    
       
        