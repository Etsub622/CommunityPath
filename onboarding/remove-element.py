class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # nums.sort()
        # l,r=0,len(nums)-1
        # while l<=r:
        #     if nums[l]!=val:
        #         l+=1
        #     if nums[r]!=val:
        #         r-=1
        # while r+1<len(nums):
        #     nums[l]=nums[r+1]
        #     r+=1
        #     l+=1
        # return l    

        l=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[l]=nums[i]
                l+=1
        return l        
