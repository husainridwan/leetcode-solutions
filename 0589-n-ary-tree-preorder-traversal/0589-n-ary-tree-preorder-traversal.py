"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        
        stack = [root]
        output = []
        
        while stack:
            #Remove the last element of the stack and save it in temp 
            tmp = stack.pop()
            output.append(tmp.val)
            #Add the children in reverse order
            stack.extend(tmp.children[::-1])
        return output