#my solution - o(n) time, but o(n) in space also because of growing list size. Do it in place for o(1) space. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        count = 1
        o = list()
        e = list()
        while t:
            if count % 2 == 0:
                e.append(t.val)
            else:
                o.append(t.val)
            count += 1
            t = t.next
            
        o = o[::-1]
        t = head
        while t and len(o) > 0:
            t.val = o.pop()
            t = t.next
        
        e = e[::-1]
        while t and len(e) > 0:
            t.val = e.pop()
            t = t.next
        
        return head

#more intuitive solution

def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        odd = head
        even = head.next
        evenHead = head.next
        
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = evenHead
        
        return head