class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check = {}
        
        for num in nums:
            if num not in check:
                check[num] = 1
            else:
                return num
            