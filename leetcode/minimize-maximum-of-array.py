class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        psum=[0]*(len(nums))
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            psum[i]=acc
        curMax=nums[0]
        for i in range(1,len(nums)):
            curMax=max(psum[i]/(i+1),curMax)
        return (math.ceil(curMax))    
    








             

        