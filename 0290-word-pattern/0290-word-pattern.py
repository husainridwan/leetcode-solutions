class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        arr = s.split()
        if len(arr) != len(pattern):
            return False
        
        for i in range(len(arr)):
            if pattern.find(pattern[i]) != arr.index(arr[i]):
                return False
            
        return True