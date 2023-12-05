class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        final=0
        output=0
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1]>nums[i+2]:
                output=sum(nums[i:i+3])
                final=max(final,output)
        return final        


        