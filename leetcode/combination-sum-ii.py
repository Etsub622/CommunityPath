class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def backtrack(idx,comb,total):    
            if total==target:
               ans.append(comb.copy())
               return 
            else:
                if total>target or idx>=len(candidates):
                    return
                 
            comb.append(candidates[idx])
            backtrack(idx+1,comb,total+candidates[idx])
            comb.pop()
            cur=candidates[idx]
            while idx<len(candidates) and  cur==candidates[idx]:
                idx+=1

            backtrack(idx,comb,total)    



                    
        backtrack(0,[],0)
        return ans  
        