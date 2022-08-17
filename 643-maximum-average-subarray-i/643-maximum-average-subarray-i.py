class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        for i in range(0, len(nums)-k):
            currSum += nums[i+k] - nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum/k