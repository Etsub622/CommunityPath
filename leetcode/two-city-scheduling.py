class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        output=0
        n=len(costs)
        for i in range(n):
            if i<(n//2):
                output+=costs[i][0]
            else:
                output+=costs[i][1]
        return output        

        