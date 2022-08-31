class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        currSum = maxSum = nums[0]
        for num in nums[1:]:
            currSum = max(currSum+num, num)
            maxSum = max(maxSum, currSum)
        return maxSum
        