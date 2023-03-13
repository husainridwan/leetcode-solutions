class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elementSum = sum(nums)
        digitSum = sum(list(map(int, ''.join(str(x) for x in nums))))           
            
        return abs(elementSum - digitSum)
        
        