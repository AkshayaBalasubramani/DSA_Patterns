# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        p=set()
        
        while curr:
            if curr in p:
                return curr
            p.add(curr)
            curr=curr.next
        return
        
        