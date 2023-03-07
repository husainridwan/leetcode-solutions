class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # If there are m number not missing,
        # that is A[0], A[1] .. A[m-1],
        # the number of missing under A[m] is A[m] - 1 - m.
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)//2
            if arr[mid] - mid - 1 < k:
                l = mid + 1
            else:
                r = mid
        return l + k