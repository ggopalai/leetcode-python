# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t = head
        c = 0
        
        while t:
            c += 1
            t = t.next
            
        if not c or not k:
            return head
        
        k = k % c
        
        def rotate(head):
            q = None
            t = head
            
            while t.next:
                q = t
                t = t.next
            
            t.next = head
            q.next = None
            
            return t
        
        a = head
        for i in range(k):
            a = rotate(a)
        
        return a

# O(n) solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # empty node
        if not head:
            return None
        
        # count number of nodes
        n = 1
        t = head
        while t.next:
            n += 1
            t = t.next
        # og last node
        last = t
        
        # actual number of rotations
        k = k % n
        if n == 1 or k == 0:
            return head
        
        # new last node
        skips = (n - k) - 1
        t = head
        while skips:
            t = t.next
            skips -= 1
        nh = t.next
        
        # swap pointers
        last.next = head
        t.next = None

        return nh











