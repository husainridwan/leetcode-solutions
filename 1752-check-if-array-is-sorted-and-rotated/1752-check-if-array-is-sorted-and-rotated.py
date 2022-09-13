class Solution:
    def check(self, nums: List[int]) -> bool:
        #Sort the list
        numSort = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i:] + nums[:i] == numSort:
                return True
        return False