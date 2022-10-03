class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        details = []
        ph = dict(zip(heights, names))

        for i in sorted(heights):
            details.append(ph[i])
        return details[::-1]