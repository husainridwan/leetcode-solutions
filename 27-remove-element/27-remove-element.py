class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        """l = 0
        for r in range(len(nums)):
            if val != nums:
                nums.remove(val)
            l += 1
        return l"""
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i