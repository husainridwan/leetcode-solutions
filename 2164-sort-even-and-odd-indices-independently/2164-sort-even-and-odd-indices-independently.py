class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even, odd, final = [], [], []
        
        for i in range(len(nums)):
            if i % 2 != 0:
                odd.append(nums[i])
            else:
                even.append(nums[i])
                
        even.sort()
        odd.sort(reverse=True)
        minlen = min(len(even), len(odd))
        for i in range(minlen):
            final.append(even[i])
            final.append(odd[i])
        if len(even) == minlen:
            final += odd[minlen:]
        else:
            final += even[minlen:]
        return final
        