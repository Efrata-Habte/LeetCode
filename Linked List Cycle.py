# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy=ListNode(0,head)
        fast=dummy
        slow=dummy
        if not fast.next:
            return False
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False
        
