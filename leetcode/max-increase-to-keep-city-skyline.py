class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans=0
        rowMax,colMax=[],[]
        for i in range(len(grid)):
            rmax,jmax=0,0
            for j in range(len(grid[0])):
                rmax=max(rmax,grid[i][j])
                jmax=max(jmax,grid[j][i])
            rowMax.append(rmax)
            colMax.append(jmax) 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans+=min(rowMax[i],colMax[j])-grid[i][j]
        return ans             


        