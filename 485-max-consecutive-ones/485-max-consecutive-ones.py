class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        for i in nums:
            if i == 1:
                count += 1
                maximum = max(maximum, count)
            else:
                maximum = max(maximum, count)
                count = 0
        return max(maximum, count)