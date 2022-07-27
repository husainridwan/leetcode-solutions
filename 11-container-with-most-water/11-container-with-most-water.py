class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, maxArea = 0, len(height) - 1, 0
        while (l < r):
            maxArea = max(maxArea, (min(height[l], height[r])*(r-l)))
            if (height[l] <= height[r]):
                l += 1
            else:
                r -= 1
        return maxArea