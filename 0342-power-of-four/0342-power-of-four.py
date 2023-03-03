class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #Checking if n is divisible by 4
        while n % 4 == 0 and n > 0:
            #Keep dividing by 4 until it can't and return true/false if remainder is equal to 1
            return self.isPowerOfFour(n/4)
        return n == 1
        