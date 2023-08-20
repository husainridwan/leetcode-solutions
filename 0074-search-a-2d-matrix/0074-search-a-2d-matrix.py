class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows*cols - 1
        
        while(l <= r):
            mid = (l+r)//2
            midEl = matrix[mid//cols][mid%cols]
            
            if midEl == target:
                return True
            elif midEl < target:
                l = mid + 1
            else:
                r = mid - 1
        return False