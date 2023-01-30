# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        #Using two pointers
        curr = head
        prev = head
        while curr.next:
            curr = curr.next
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
                
        if head.val == val:
            return head.next
        return head
        
        