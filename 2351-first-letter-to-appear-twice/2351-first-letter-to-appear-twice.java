class Solution:
    def repeatedCharacter(self, s: str) -> str:
        check = {}
        count = 1
        
        for char in s:
            if char not in check:
                check[char] = 1
            elif check[char] == count:
                return char
            else:
                check[char] += 1