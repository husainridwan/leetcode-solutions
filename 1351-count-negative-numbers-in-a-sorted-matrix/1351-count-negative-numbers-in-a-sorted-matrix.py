class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid[0])
        cols = len(grid)
        neg = 0
        
        l, r = 0, rows - 1
        
        while l < cols and r >= 0:
            if grid[l][r] < 0:
                neg += cols - l
                r -= 1
            else:
                l += 1
        return neg