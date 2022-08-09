class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totalsum = n*(n+1)//2

        for num in nums:
	        totalsum -= num

        return totalsum
        