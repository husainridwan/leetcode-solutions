# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isSame(root.left, root.right)
    
    def isSame(self, leftroot, rightroot):
        #If the left & right node are both null, it will return True
        if leftroot == None and rightroot == None:
            return True
        #If only one of the nodes is equal to null, return False
        if leftroot == None or rightroot == None:
            return False
        if leftroot.val != rightroot.val:
            return False
        
        return self.isSame(leftroot.right, rightroot.left) and self.isSame(leftroot.left, rightroot.right)
        