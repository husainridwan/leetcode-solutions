class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #return n > 0 and (1 << 31) % n == 0
        if n == 1:
            return True
    
        if n < 1:
            return False
    
        return self.isPowerOfTwo(n/2)