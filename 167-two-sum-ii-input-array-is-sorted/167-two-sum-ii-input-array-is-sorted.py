class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        checkSum = {}
        for i, x in enumerate(numbers):
            y = target - x
            if y in checkSum:
                return [checkSum[y]+1, i+1]
            else:
                checkSum[x] = i
        return []
        