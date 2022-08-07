class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for i in nums:
            if i not in check:
                check[i] = 1 
            else:
                return True
        return False
            