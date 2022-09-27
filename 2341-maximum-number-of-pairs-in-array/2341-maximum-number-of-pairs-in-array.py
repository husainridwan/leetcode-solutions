class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        check = {}
        for num in nums:
            check[num] = check.get(num, 0) + 1
            
        count = 0
        sec_count = 0
        for i in check:
            count += (check[i]//2)
            sec_count += (check[i]%2)
            
        return [count, sec_count]