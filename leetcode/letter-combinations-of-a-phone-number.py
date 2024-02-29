class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        ans=[]
        def backtrack(idx,comb):
            if len(comb)==len(digits):
                ans.append(''.join(comb.copy()))
                return

            for i in range(idx,len(digits)):
                lst=letter[(digits[i])]
                for j in range(len(lst)):
                    comb.append(lst[j])
                    backtrack(i+1,comb)
                    comb.pop()
        backtrack(0,[])  
        return ans if ans!= [""] else []
        
