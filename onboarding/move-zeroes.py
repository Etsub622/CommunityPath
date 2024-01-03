class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        for i in nums:
            if i!=0:
                nums[l]=i
                l+=1
        while l<len(nums):
            nums[l]=0
            l+=1        
        
        
                
               



        