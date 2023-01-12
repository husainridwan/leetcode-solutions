# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = []
        curr = [root] #traverses one level at a time
        
        while curr :
            q.append(curr)
            curr = []
            for node in q[-1] :
                # q of -1 means basically the most recently added level of the binary tree to the q
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
        values = [[node.val for node in curr] for curr in q ]
        
        return([sum(level)/len(level) for level in values])
    