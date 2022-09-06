class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Using Binary Search
        l = 0
        r = len(nums) - 1
        
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if target >= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l