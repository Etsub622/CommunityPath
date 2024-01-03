class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # output=0
        # l=0
        
        # while l<len(nums):
        #     for i in range(len(nums)):
        #         if l<i and nums[l]+nums[i]<target:
        #            output+=1
        #     l+=1        
        # return output   

        nums.sort()
        output=0
        l,r=0,len(nums)-1
        while l<r:
            if nums[l]+nums[r]<target:
                output+=r-l
                l+=1
            else:
                r-=1
        return output            


        