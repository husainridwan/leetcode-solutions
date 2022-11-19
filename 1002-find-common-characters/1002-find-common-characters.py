class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = list(words[0])
        
        for word in words:
            newCheck = []
            for char in word:
                if char in check:
                    newCheck.append(char)
                    check.remove(char)
            check = newCheck
        return newCheck