class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates=[1,2,3,4,5,6,7,8,9]
        candidates.sort()
        ans=[]
        def backtrack(idx,comb,total):    
            if total==n and len(comb.copy())==k:
               ans.append(comb.copy())
               return 
            else:
                if total>n or idx>=len(candidates):
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