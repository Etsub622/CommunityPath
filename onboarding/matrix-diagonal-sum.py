class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = {}
        for i in range(n):
            for j in range(n):
                if i - j == 0:
                    total[i - j] = total.get(i - j, 0) + mat[i][j]
            for j in range(n):        
                if i + j == n - 1 and i!=j :
                    total[i + j] = total.get(i + j, 0) + mat[i][j]

        output = 0
        for val in total.values():
            output += val
        return output  




        