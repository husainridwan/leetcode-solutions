class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if m*n == len(original):
            for i in range(0, len(original), n):
                result.append(original[i:i+n])
        return result
                
        