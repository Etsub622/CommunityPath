class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic=Counter(nums)
        coun=0
        for i in dic:
            n=dic[i]
            if n>=2:
                coun+=(n*(n-1)//2)

        return coun 