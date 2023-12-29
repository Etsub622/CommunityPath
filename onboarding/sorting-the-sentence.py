class Solution:
    def sortSentence(self, s: str) -> str:
        output=[]
        words=s.split()
        for word in words:
            output.append([int(word[-1]),word[:len(word)-1]])

        output.sort() 
        res=[]
        for i,val in output:
            res.append(val)

        return ' '.join(res)  
        