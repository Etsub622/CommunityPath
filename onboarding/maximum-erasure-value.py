class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        Set=set()
        output=float("-inf")
        for i in range(len(nums)):       
            while nums[i] in Set:
                Set.remove(nums[l])
                l+=1
            Set.add(nums[i])    
            output=max(output,sum(Set))
        return output    








        