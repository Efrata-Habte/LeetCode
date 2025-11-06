# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        fast=head
        while fast:
            stack.append(fast.val)
            fast=fast.next

        fast=head
        while fast:
            last=stack.pop()
            if fast.val!=last :
                return False
            fast=fast.next
        return True
        
        
