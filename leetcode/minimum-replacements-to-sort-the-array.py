class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        min_num = nums[-1]
        for i in range(len(nums)-2, -1,-1):
            div= ceil(nums[i]/ min_num) 
            ans+= div - 1 
            min_num= nums[i]//div 
        return ans
       