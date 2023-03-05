class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = dict(), dict()
        for x, y in zip(s, t):
            if (x in d1 and d1[x] != y) or (y in d2 and d2[y] != x):
                return False
            d1[x], d2[y] = y, x
        return True