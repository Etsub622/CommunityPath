class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current,l=sum(nums[:k]),0
        max_sum=current
        for i in range(k,len(nums)):
            current+=nums[i]
            current-=nums[l]
            max_sum=max(max_sum,current)
            l+=1
                
        return max_sum/k       


        