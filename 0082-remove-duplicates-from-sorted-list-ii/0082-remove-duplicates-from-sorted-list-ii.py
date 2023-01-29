# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            # If there's no duplicate,
            # move prev and cur one step forward
            if curr.val != curr.next.val:
                prev, curr = curr, curr.next
                
            else:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                #skipping the duplicate
                prev.next = curr.next
                curr = curr.next
                
        return dummy.next
       