class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #Using XOR and reversing first
        return [[1^i for i in img[::-1]] for img in image]
    