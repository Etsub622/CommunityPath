class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        final=[]
        n=len(nums)
        for i in range(n):
            count=0
            for j in range(n):
                if j!=i and nums[i]>nums[j]:
                    count+=1
            final.append(count)
        return final   
            