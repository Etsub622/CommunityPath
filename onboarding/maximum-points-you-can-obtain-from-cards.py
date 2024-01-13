class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        # while  k>0 and l<=r:
        #     if cardPoints[r]>=cardPoints[l]:
        #         output+=cardPoints[r]
        #         r-=1
        #     else:
        #         output+=cardPoints[l]
        #         l+=1
        #     k-=1    
        # return output

        l,n=len(cardPoints),0
        m=n-k
        current,l=sum(cardPoints[:m]),0
        min_sum=current
        for i in range(m,n):
            current+=cardPoints[i]
            current-=cardPoints[l]
            min_sum=min(min_sum,current)
            l+=1   
        total=sum(cardPoints)
        return total- min_sum    





        