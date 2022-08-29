class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = {}
        total = 0
        
        for i in nums:
            if i in pairs:
                if pairs[i] == 1:
                    total += 1
                else:
                    total += pairs[i]
                pairs[i] += 1
            else:
                pairs[i] = 1
        return total
