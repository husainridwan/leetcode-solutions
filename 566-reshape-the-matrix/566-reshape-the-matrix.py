class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        
        try:
            return np.reshape(mat, (r, c)).tolist()
        except:
            return mat