"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        
        stack = [root]
        output = []
        while stack:
            tmp = stack.pop()
            output.append(tmp.val)
            stack.extend(tmp.children)
            
        return output[::-1]