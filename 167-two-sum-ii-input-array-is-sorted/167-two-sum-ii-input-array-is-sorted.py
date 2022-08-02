class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """checkSum = {}
        for i, x in enumerate(numbers):
            y = target - x
            if y in checkSum:
                return [checkSum[y]+1, i+1]
            else:
                checkSum[x] = i
        return []"""
    
        l = 0
        r = len(numbers) - 1
        while (numbers[l] + numbers[r]) != target:
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]
        