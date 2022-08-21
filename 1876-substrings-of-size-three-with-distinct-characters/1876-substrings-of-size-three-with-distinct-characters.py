class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        dis = 0
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == 3:
                dis += 1
        return dis
        