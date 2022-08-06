class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        l, maxF = 0, 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])
            
            while ((r - l + 1) - maxF) > k:
                count[s[l]] -= 1
                l += 1
            result = max(r - l + 1, result)
        return result
                   
        
        