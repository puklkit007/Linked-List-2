# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lena = 0
        lenb = 0
        curr = headA
        
        while curr is not None:
            lena += 1
            curr = curr.next
        curr = headB
        while curr is not None:
            lenb += 1
            curr = curr.next
            
        diff = abs(lena - lenb)
        if lena > lenb:
            while diff > 0:
                headA = headA.next
                diff -= 1
        else:
            while diff > 0:
                headB = headB.next
                diff -= 1
            
        while headA != headB:
            headA = headA.next
            headB = headB.next
            
        return headA
            
