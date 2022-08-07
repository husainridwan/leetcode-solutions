class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """nums.sort()
        return nums[len(nums)//2]"""
    
        check = {}
        for i in nums:
            check[i] = check.get(i, 0) + 1
            if check[i] > len(nums)//2:
                return i
        

            
        