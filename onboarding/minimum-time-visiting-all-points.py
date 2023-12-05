class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        output=0
        for i in range(len(points)-1):
            res=max( abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1]))
            output+=res
        return output    
            
        