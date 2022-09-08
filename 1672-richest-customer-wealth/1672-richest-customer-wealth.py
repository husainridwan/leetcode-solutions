class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0
        for account in accounts:
            curSum = sum(account)
            if maxSum < curSum:
                maxSum = max(maxSum, curSum)
        return maxSum