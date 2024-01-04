class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l,r,output=0,0,0
        g.sort()
        s.sort()
        while l<len(s) and r<len(g):
            if s[l]>=g[r]:
                output+=1
                l+=1
                r+=1
            else:
               
                l+=1
        return output        

            