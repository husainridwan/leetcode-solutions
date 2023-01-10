class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        check = {}
        for num in nums:
            if num in check:
                check[num] += 1
            else:
                check[num] = 1
                
        dups = []
        for num in check:
            if check[num] == 2:
                dups.append(num)
        return dups