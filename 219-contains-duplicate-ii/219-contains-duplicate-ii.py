class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = {}
        for i, j in enumerate(nums):
            if j in check and i - check[j] <= k:
                return True
            check[j] = i
        return False