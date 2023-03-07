class Solution(object):
    def leftRigthDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 0
        suffix = sum(nums)
        ans = []
        
        for num in nums:
            prefix += num
            ans.append(abs(prefix - suffix))
            suffix -= num
        return ans