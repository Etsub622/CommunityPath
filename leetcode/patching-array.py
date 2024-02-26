class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        psum=0
        output=0
        l=0 
        while psum<n:
            if l<len(nums) and nums[l]<=psum+1:
                psum+=nums[l]
                l+=1
                
            else:
                psum+=psum+1
                output+=1
               
        return output    
             

        