class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct=len(set(nums))
        output,l=0,0
        dic=defaultdict(int)
        
        for i in range(len(nums)):
            dic[nums[i]]+=1
        
            while len(dic)==distinct:
                output+=len(nums)-i
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    del dic[nums[l]]
                l+=1
                
        return output     



               




        