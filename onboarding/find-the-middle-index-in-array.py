class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        acc=0
        pSum=[0]
        for i in nums:
            acc+=i
            pSum.append(acc)
            
        for j in range(1,len(pSum)):
            if pSum[j-1]==pSum[-1]-pSum[j]:
                return j-1
        return -1        

        