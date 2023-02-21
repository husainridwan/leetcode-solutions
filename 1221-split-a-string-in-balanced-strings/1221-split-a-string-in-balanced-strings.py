class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = count = 0
        for i in s:
            count += 1 if i == 'L' else -1
            if count == 0:
                result += 1
        return result