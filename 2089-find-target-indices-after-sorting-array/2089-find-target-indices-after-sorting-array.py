class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        check = []
        for i in range(len(nums)):
            if nums[i] == target:
                check.append(i)
        return check

                
        