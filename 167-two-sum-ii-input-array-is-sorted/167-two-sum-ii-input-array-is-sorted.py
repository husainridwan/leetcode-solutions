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
        while l < r:
            total = numbers[l] + numbers[r]
            if target == total:
                return [l+1, r+1]
            elif total > target:
                r -= 1
            else:
                l += 1
        return []
        