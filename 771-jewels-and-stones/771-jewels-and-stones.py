class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #count = 0
        #jewels = set(jewels)
        #for i in stones:
        #    if i in jewels:
        #        count += 1
        #return count
        
        return sum(i in jewels for i in stones)