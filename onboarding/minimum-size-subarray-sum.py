class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,res,output=0,0,len(nums)+1
        for i in range(len(nums)):
            res+=nums[i]
            while res>=target:
                output=min(output,i-l+1)
                res-=nums[l]
                l+=1
            
        return output if output!=len(nums)+1 else 0   






            
               