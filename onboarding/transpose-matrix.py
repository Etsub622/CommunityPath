class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output=[]
        for i in range(len(matrix[0])):
            column=[]
            for j in matrix:    
                column.append(j[i])
            output.append(column)
        return output            


        