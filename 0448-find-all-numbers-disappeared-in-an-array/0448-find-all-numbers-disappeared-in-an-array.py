class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [i for i in range(1, len(nums)+1)]
        dis = list(set(arr) - set(nums))
        return dis