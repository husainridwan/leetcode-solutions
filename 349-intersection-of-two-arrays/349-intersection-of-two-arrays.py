class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """nums1 = set(nums1)
        nums2 = set(nums2)
        
        return list(nums2 & nums1)"""
    
        nums3 = [x for x in nums1 if x in nums2]
        return list(set(nums3))
        
        