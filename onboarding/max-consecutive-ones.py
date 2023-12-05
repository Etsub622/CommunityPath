class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output=0
        final=output
        for i in nums:
            if i==1:
                output+=1
                final=max(output,final)
            else:
                
                output=0

        return final            
        