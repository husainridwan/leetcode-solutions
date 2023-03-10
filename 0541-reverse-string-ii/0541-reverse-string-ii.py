class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        word = list(s)
        for i in xrange(0, len(word), k*2):
            word[i:i+k] = reversed(word[i:i+k])
        return "".join(word)