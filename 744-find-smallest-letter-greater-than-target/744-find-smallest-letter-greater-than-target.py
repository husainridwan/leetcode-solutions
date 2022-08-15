class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """for i in letters:
            if i > target:
                return i
        return letters[0]"""
        #If the target is out of bounds
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        #Using binary search
        l = 0
        r = len(letters) - 1
        while l <= r:
            mid = (l+r)//2
            if target >= letters[mid]:
                l = mid + 1
                
            if target < letters[mid]:
                r = mid - 1
        return letters[l]