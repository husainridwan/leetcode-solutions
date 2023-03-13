class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxNum = max(nums)
        minNum = min(nums)
        return max(0, maxNum - k - (minNum+k))