class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maximum = 0
        for i in nums:
            if i == 1:
                count += 1
                maximum = max(count, maximum)
            else:
                maximum = max(count, maximum)
                count = 0
        return max(count, maximum)