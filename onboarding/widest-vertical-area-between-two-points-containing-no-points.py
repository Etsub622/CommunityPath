class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        widestPoint=0
        for  i in range(len(points)-1):
            widestPoint=max(widestPoint,points[i+1][0]-points[i][0])
        return widestPoint    
        

