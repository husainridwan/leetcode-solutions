class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        while i<len(nums)-1:
            if nums[i]>nums[i+1]: break    # used to find the rotated position
            i+=1
        
        rotated = nums[i+1:]+nums[:i+1]
        for i,e in enumerate(rotated):
            if i<len(rotated)-1 and e>rotated[i+1]:   # check that rerotated array sorted or not
                return False
        return True 