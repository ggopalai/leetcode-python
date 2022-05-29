#my solution 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def formList(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        
        t = head
        while t.next:
            t = t.next
        t.next = ListNode(val)
        
        return head
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        num1 = str()
        num2 = str()
        while a:
            num1 = str(a.val) + num1
            a = a.next
        while b:
            num2 = str(b.val) + num2
            b = b.next 
        
        res = int(num1) + int(num2)
        if res == 0:
            return ListNode(0)
        
        x = res
        head = ListNode(999)
        while x:
            r = x % 10
            x = x // 10
            head = self.formList(head, r)
        
        return head.next


# elementary math addition method - 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy 
        
        carry = 0
        while l1 or l2 or carry:  #or carry takes care of edge case where last step has carry over
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            dig = val % 10
            carry = val // 10
            
            cur.next = ListNode(dig)
            cur = cur.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        
        return dummy.next