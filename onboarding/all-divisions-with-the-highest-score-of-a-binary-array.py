class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        count = [0]
        divScore=sum(nums)
        maxScore =divScore   
        
        for i,val in enumerate(nums,1):
            if val==0:
                divScore+=1
            else:
                divScore-=1    
            
            if divScore > maxScore:
                maxScore = divScore
                count = [i]
            elif divScore == maxScore:
                count.append(i)
        
        return count   
        
            

        