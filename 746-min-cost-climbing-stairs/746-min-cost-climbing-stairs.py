class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        
        #Using recursion
        total = [0] * len(cost)
        total[0] = cost[0]
        if len(cost) >= 2:
            total[1] = cost[1]
            
        for i in range(2, len(cost)):
            total[i] = cost[i] + min(total[i-2], total[i-1])
        
        return min(total[-1], total[-2])