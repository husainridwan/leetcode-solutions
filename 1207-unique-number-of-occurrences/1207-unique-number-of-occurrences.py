class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        check, ans = {}, []
        for i in arr:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1
        
        for i in check:
            ans.append(check[i])
        return sorted(ans) == sorted(set(ans))