class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.binarySearch(nums, target, True)
        last = self.binarySearch(nums, target, False)
        return [first, last]
        
    def binarySearch(self, nums, target, leftBias):    
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
        """l = 0
        r = len(nums)-1
        res = [-1,-1]
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                res[0]=mid #to store the position where target is found
                r = mid -1 #to move the pointer to further left in order to find the first                      pos
            elif nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid +1
                
        l = 0
        r = len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                res[1] = mid #to store the position where target is found
                l = mid +1 #to move the pointer to further right to find the first pos
            elif nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid +1
                
        return res"""
        