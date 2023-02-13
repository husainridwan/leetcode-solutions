class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        for num in nums:
            subset += [i+[num] for i in subset]
        return subset