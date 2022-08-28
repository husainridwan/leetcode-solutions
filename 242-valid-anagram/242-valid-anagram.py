class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = "abcdefghijklmnopqrstuvwxyz"
        for i in letters:
            if s.count(i) != t.count(i):
                return False
        return True
    