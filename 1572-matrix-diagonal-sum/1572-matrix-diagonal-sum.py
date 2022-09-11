class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        total = 0
        
        for i in range(rows):
            for j in range(cols):
                if i == j or i+j == rows - 1:
                    total += mat[i][j]
        return total
        