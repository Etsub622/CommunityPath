class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        matrix = [['.'] * n for _ in range(m)]
        for guard in guards:
            row, col = guard
            matrix[row][col] = 'G'

        for wall in walls:
            row, col = wall
            matrix[row][col] = 'W'
        print(matrix)    

        Set = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'G':
                    # Check north
                    for r in range(i - 1, -1, -1):
                        if matrix[r][j] != '.':
                            break
                        Set.add((r, j))
                    # Check south
                    for r in range(i + 1, m):
                        if matrix[r][j] != '.':
                            break
                        Set.add((r, j))
                    # Check west
                    for c in range(j - 1, -1, -1):
                        if matrix[i][c] != '.':
                            break
                        Set.add((i, c))
                    # Check east
                    for c in range(j + 1, n):
                        if matrix[i][c]!='.':
                            break
                        Set.add((i, c))

        outcome = (n * m) - (len(guards) + len(walls) + len(Set))
        return outcome