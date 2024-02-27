class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        def backtrack(idx,comb,total):
            
            if total==target:
    
               ans.append(comb.copy())
               return 
            else:
                if total>target:
                    return
                 
            for i in range(idx,len(candidates)):
                if candidates[i]>target:
                    pass
                else:
                    comb.append(candidates[i])
                    backtrack(i,comb,total+candidates[i])
                    comb.pop()
        backtrack(0,[],0)
        return ans               

