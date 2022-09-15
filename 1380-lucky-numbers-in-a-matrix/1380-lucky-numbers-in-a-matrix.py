class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rmin = {min(row) for row in matrix}
        cmax = {max(col) for col in zip(*matrix)}
        return list(rmin & cmax)