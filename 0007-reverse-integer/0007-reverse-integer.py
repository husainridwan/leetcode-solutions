class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        
        if rev.bit_length() > 31:
            return 0
        if x < 0:
            return -1*rev
        else:
            return rev