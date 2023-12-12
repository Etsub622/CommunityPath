class Solution:
    def reverseWords(self, s: str) -> str:
        sSplited=s.split()
        sFinal=[]
        for i in reversed(sSplited):
            if i=='':
                pass
            else:
                sFinal.append(i)    
        return " ".join(sFinal)   

        