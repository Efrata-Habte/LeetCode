# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        stack=[]

        while fast:
            stack.append(fast.val)
            fast=fast.next
        fast=head
        while fast:
            last=stack.pop()
            fast.val=last
            fast=fast.next
        return head
