class Solution:
    def maxScore(self, s: str) -> int:
        pSum=[0]
        acc=0
        for i in s:
            acc+=int(i)
            pSum.append(acc)

        maxScore=0
        for i in range(1,len(pSum)-1):
            score = (i -pSum[i]) + (pSum[-1] - pSum[i])
            maxScore=max(score,maxScore)

        return maxScore    


        