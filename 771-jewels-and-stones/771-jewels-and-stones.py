class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result, count = 0, {}
        
        for i in stones:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            
        for i in jewels:
            if i in count:
                result += count[i]
        return result
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                