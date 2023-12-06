class Solution:
    def numberOfMatches(self, n: int) -> int:
        i=n
        output=0
        while i>1:
            if i%2==0:
                output+=i//2
                i=i//2
                
            else:
                output+=(i-1)//2+1
                i=(i-1)//2    
        return output  


           



              

        