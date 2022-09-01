class Solution(object):
    def twoSum(self, nums, target):
        """check = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in check:
                return [check[y], i]
            else:
                check[x] = i    
        return []"""
    
        l, r = 0, len(nums) - 1
        arr = []
        for i in range(len(nums)):
            arr.append([nums[i], i])
            
        arr.sort()
        while l < r:
            if arr[l][0] + arr[r][0] == target:
                return [arr[l][1], arr[r][1]]
            elif arr[l][0] + arr[r][0] < target:
                l += 1
            else:
                r -= 1
        return -1
        