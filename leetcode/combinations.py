class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backtrack(idx,comb):
            if len(comb)==k:
                ans.append(comb.copy())
                return

            for i in range(idx,n-(k-len(comb))+2):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
        backtrack(1,[])  
        return ans     
                   