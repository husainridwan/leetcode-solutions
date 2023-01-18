# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #Check if the root has a left child, if yes, add its curr val to the left child in the right sub-tree
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        #Else check for left child in both subtrees
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)