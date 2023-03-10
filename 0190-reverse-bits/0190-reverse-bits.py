class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        revNum = 0
        for i in range(32):
            #Left shift the reversed number by 1 and add the last bit of the given number
            revNum = (revNum << 1) | (n&1)
            n >>= 1
        return revNum
            