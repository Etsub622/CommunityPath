class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output=[]
        n,m=len(mat),len(mat[0])
        row,col=0,0
        upRight=True
        for i in range(n*m):
            output.append(mat[row][col])
            if upRight:
                if row==0 and col<m-1:
                    upRight=False
                    col+=1
                elif col==m-1:
                    upRight=False
                    row+=1
                else:
                    row-=1
                    col+=1
            else:
                if col==0 and row<n-1:
                    upRight=True
                    row+=1
                elif row==n-1:
                    upRight=True
                    col+=1
                else:
                    row+=1
                    col-=1
        return output            

                    




        
  
        