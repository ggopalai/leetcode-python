# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Brute force.
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        import sys
        sys.set_int_max_str_digits(10001) # fails without this

        t = head
        s = 0
        
        # extract the numbers
        while t:
            s = s * 10 + t.val
            t = t.next
        
        # double it
        n = s * 2

        dummy = ListNode()
        cur = dummy
        for c in str(n):
            cur.next = ListNode(c)
            cur = cur.next 
        
        return dummy.next

# 2. Can be a special case of add two numbers.
            





        