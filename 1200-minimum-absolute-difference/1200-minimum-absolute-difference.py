class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        mini, res = abs(arr[1] - arr[0]), [arr[0:2]]
        for i in range(2, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            
            if diff > mini:
                continue

            if diff < mini:
                mini, res = diff, list()
                
            res.append([arr[i - 1], arr[i]])
                
        return res