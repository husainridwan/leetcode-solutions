class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        odd, even = 0, 0
        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)