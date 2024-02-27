class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(idx,comb):
            if len(comb)==len(nums):
                ans.append(comb.copy())
                return 
            for i in range(len(nums)):
                if nums[i] in comb.copy():
                    pass
                else:
                    comb.append(nums[i])
                    backtrack(i+1,comb)
                    comb.pop()
               
        backtrack(0,[])
        return ans

        