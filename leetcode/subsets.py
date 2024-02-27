class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(idx,subset):
            i=0
            if i<len(nums):
                ans.append(subset.copy())          
                i+=1
               
            for i in range(idx,len(nums)):
                if nums[i] in subset.copy():
                    pass
                else:
                    subset.append(nums[i])
                    backtrack(i+1,subset)
                    subset.pop()
        backtrack(0,[])
        return ans                
                            

        