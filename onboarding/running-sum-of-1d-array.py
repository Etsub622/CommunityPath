class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pSum=[]
        acc=0
        for i in nums:
            acc+=i
            pSum.append(acc)
        return pSum    