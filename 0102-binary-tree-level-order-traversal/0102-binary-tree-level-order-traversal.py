# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        answer = []
        q = deque([root, None])
        level = [] #To track the current level
        
        while q:
            node = q.popleft()
            if node:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
                
            elif not node and not q:
                break

            elif not node:
                answer.append(level)
                level = []
                q.append(None)
                    
        #Accounting or the final level
        if level:
            answer.append(level)
        return answer
        
        
     