class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            rowChecker = set()
            columnChecker = set()
            subBoxChecker = set()
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in rowChecker:
                    return False
                else:
                    rowChecker.add(board[i][j])
                
                
                if board[j][i] != '.' and board[j][i] in columnChecker:
                    return False
                else:
                    columnChecker.add(board[j][i])
                
                
                row = 3 * (i // 3) + j // 3
                col = 3 * (i % 3) + j % 3
                if board[row][col] != '.' and board[row][col] in subBoxChecker:
                    return False
                else:
                    subBoxChecker.add(board[row][col])
        
        return True