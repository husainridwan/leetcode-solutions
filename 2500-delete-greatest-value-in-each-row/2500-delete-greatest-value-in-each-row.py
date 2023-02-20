class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            grid[i].sort()
            
        grid = list(zip(*grid))
        
        return (sum(max(row) for row in grid))