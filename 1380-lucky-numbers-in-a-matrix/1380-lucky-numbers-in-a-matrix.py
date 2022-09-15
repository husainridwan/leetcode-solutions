class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        #rmin = {min(row) for row in matrix}
        #cmax = {max(col) for col in zip(*matrix)}
        #return list(rmin & cmax)
    
        rmin = [min(r) for r in matrix]
        cmax = []
        
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            cmax.append(max(temp))
        return set(rmin) & set(cmax)