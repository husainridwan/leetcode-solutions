class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        
        #Condition to ensure r does not exceed length of array
        while r < len(prices):
            #Check if profitable
            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
                
        