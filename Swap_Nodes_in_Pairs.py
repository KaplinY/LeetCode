# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head and head.next): return head 

        result = head.next
        head.next, result.next = self.swapPairs(head.next.next), head
        return result
