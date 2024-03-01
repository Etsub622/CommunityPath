class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def generate(open,close,curr):
            if open==0 and close==0:
                ans.append(''.join(curr))
                return
            
            if open>0:           
                o=open-1
                curr.append('(')
                generate(o,close,curr)
                curr.pop() 
           
            if close >open:
                c=close-1
                curr.append(')') 
                generate(open,c,curr)
                curr.pop()
            
        generate(n,n,[]) 
        return ans          


        