class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        checkSum = {}
        for i, x in enumerate(numbers):
            if target - x in checkSum:
                return [checkSum[target-x]+1, i+1]
            else:
                checkSum[x] = i
        return []
    
        """l, r = 0, len(numbers) - 1
        while (numbers[l] + numbers[r]) != target:
            if (numbers[l] + numbers[r]) > target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]"""
        