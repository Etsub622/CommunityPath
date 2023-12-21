class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        # possible=[(0,0),(0,1),(0,2),(1,1),(2,0),(2,1),(2,2)]
        partialSum=0
        final=float('-inf')
        for i in range(len(grid)-2):
            partialSum=0
            for j in range(len(grid[0])-2):
                if i+2 and j+2:
                    partialSum=grid[i][j] + grid[i][j+1] +grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                    
                    final=max(final,partialSum)
        return final


        