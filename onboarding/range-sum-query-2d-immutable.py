class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.sumMatrix = [[0] * (col + 1) for r in range(row + 1)]

        for i in range(row):
            for j in range(col):
                self.sumMatrix[i + 1][j + 1] = matrix[i][j] + self.sumMatrix[i][j + 1] + self.sumMatrix[i + 1][j] - self.sumMatrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2=row1+1,col1+1,row2+1,col2+1
        result=self.sumMatrix[r2][c2]-self.sumMatrix[r2][c1-1]-self.sumMatrix[r1-1][c2]+self.sumMatrix[r1-1][c1-1]
        return result

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)