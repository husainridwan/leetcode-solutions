class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def createString(S):
            newString = []
            for i in S:
                if i != '#':
                    newString.append(i)
                elif newString:
                    newString.pop()
            return "".join(newString)
        return createString(s) == createString(t)
      