class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        #If n is even, return n, else return n * 2
        if n % 2 == 0:
            return n
        return n * 2