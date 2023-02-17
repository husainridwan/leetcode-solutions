# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #Since the previous node is unknown, nextNode won't be null
        nextNode = node.next
        #Assign the nextNode to the current node
        node.val = nextNode.val
        node.next = nextNode.next
        nextNode.next = None