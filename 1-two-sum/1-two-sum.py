class Solution(object):
    def twoSum(self, nums, target):
        check = {}
        for i, x in enumerate(nums):
            y = target - x
            if y in check:
                return [check[y], i]
            else:
                check[x] = i    
        return []