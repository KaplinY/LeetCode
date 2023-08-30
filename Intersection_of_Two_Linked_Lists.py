# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        lenB = 0
        a = headA
        b = headB
        while a:
            lenA += 1
            a = a.next
        while b:
            lenB += 1
            b = b.next
        difference = abs(lenA-lenB)
        if lenA > lenB:
            for i in range(difference):
                headA=headA.next
        else:
            for i in range(difference):
                headB=headB.next
        while headA and headB:
            if headA==headB:
                return headA
            headA=headA.next
            headB=headB.next
        