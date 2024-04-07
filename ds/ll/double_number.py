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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(head):
            if not head:
                return head
            cur, prev = head, None

            while cur:
                temp = cur.next
                cur.next = prev 
                prev = cur 
                cur = temp
            return prev
        
        newHead = reverse(head)
        temp = newHead
        dummy = ListNode(-1)
        n = dummy
        carry = 0

        while temp:
            res = temp.val * 2 + carry
            dig = res % 10
            carry = res // 10
            n.next = ListNode(dig)
            n = n.next 
            temp = temp.next 
        
        if carry:
            n.next = ListNode(carry)
        
        return reverse(dummy.next) 
        
        
            




        