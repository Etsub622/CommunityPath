class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def backtrack(idx,subset):
            if subset.copy() not in ans:
                ans.append(subset.copy())

            for i in range(idx,len(nums)):
                subset.append(nums[i])
                backtrack(i+1,subset)
                subset.pop()
        backtrack(0,[])
        return ans
            

        