class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #num1 = set(nums1)
        #num2 = set(nums2)
        
        temp1 = [x for x in set(nums1) if x not in set(nums2)]
        temp2 = [y for y in set(nums2) if y not in set(nums1)]
        
        return [temp1, temp2]