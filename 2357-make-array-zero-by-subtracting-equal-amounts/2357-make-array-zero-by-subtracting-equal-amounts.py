class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        if 0 in nums:
            return len(nums) - 1
        else:
            return len(nums)