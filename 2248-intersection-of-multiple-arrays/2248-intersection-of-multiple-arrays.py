class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        check = {}
        for i in range(len(nums)):
            for j in nums[i]:
                if j not in check:
                    check[j] = 1
                else:
                    check[j] += 1
                    
        result = []
        for k, v in check.items():
            if v == len(nums):
                result.append(k)
                
        return sorted(result)