class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = list(s.split(" "))
        for i in s:
            return " ".join(arr[:k])
        