class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=float('-inf')
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            maxi=max(maxi,acc)
            if acc<0:
                acc=0    
            
        return maxi 
        
                   