class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        mn = nums[0]
        mx = nums[-1]
        
        for i in range(mn, 0, -1):
            if mn % i == 0 and mx % i == 0:
                return i