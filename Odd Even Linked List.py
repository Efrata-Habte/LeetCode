# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even=deque()
        odd=deque()
        fast=head
        while fast and fast.next:
            odd.append(fast.val)
            fast=fast.next
            even.append(fast.val)
            fast=fast.next
        if fast:
            odd.append(fast.val)
        
        fast=head
        while fast:
            if odd:
                fast.val=odd.popleft()
            else:
                fast.val=even.popleft()
            fast=fast.next
        return head
        
