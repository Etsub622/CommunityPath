class Solution:
    def countGoodNumbers(self, n: int) -> int:
        m=10**9 + 7
        if n%2==0:
            return pow(5,n//2,m)*pow(4,n//2,m) %m
        else:
            
            return pow(5,((n-1)//2)+1,m)*pow(4,n//2,m)%m



         


