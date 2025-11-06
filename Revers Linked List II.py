# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack=[]
        fast=head
        l=1
        while fast:
            if l>=left and l<=right:
                stack.append(fast.val)
            l+=1
            fast=fast.next
        fast=head
        l=1
        while fast:
            if l>=left and l<=right:
                fast.val=stack.pop()
            l+=1
            fast=fast.next
        return head
