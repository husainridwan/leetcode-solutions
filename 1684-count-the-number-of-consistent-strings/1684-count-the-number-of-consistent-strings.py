class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allow = set(allowed)
        
        for word in words:
            len_word = len(word)
            for char in word:
                if char not in allow:
                    break
                len_word -= 1
            if len_word == 0:
                count += 1
        return count