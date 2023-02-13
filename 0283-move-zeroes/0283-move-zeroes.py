class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = 0 
        for r in range(len(nums)):
            if nums[r] != 0 and nums[l] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                
            if nums[l] != 0:
                l += 1