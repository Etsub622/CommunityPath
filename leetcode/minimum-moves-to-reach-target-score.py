class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles==0:
            return target-1
        ans=1
        n=target
        while maxDoubles>0 and n>2:
            if n%2==0:
                n=n//2
                maxDoubles-=1
                ans+=1
            else:
                n=(n-1)//2
                maxDoubles-=1
                ans+=2
        ans+=n-2
        return ans        

                


            