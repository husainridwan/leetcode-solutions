class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        total = 0
        
        #for i in range(rows):
        #    for j in range(cols):
        #        if i == j or i+j == rows - 1:
        #            total += mat[i][j]
        #return total

        #n = cols-1
        
        for i in range(rows):
		    # Add primary diagonal.
            total += mat[i][i]
			# Add the secondary but avoid the middle point that overlaps the primary.
            if i != cols-1-i:
                total += mat[i][cols-1-i]
            
        return total