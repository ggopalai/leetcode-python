# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or head.next == None:
            return False
        
        a = head
        b = head
        
        while a.next is not None and b.next is not None and b.next.next is not None:
            a = a.next
            b = b.next.next
            if id(a) == id(b):
                return True
            
        return False
        