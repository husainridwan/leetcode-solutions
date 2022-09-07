class Solution:
    def binarySearch(self, arr):
        start = 0
        end = len(arr) - 1
        while start < end:
            mid = start + ((end - start) // 2)
            if arr[mid] < 0:
                end = mid
            else:
                start = mid + 1
        return end if arr[end] < 0 else end + 1

    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        negatives = 0
        for i in range(m):
            negatives += n - self.binarySearch(grid[i])
        return negatives