class Solution:
    def repeatedCharacter(self, s: str) -> str:
        times = 1
        check = {}
        
        for char in s:
            if char not in check:
                check[char] = 1
            elif check[char] == times:
                return char
            else:
                check[char] += 1
