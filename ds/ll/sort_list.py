# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        #split up the list, the right node is the one next to the middle. 
        left, right = head, self.findMid(head)
        temp = right.next
        right.next = None
        right = temp
        
        return self.merge(self.sortList(left), self.sortList(right))
       
    def findMid(self, head):
            s, f = head, head.next
            while f and f.next:
                s = s.next
                f = f.next.next
            return s
    
    def merge(self, a, b):
        dummy = tail = ListNode()
        while a and b:
            if a.val < b.val:
                tail.next = a
                tail = tail.next
                a = a.next
            else:
                tail.next = b
                tail = tail.next
                b = b.next
        while a:
            tail.next = a
            tail = tail.next
            a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
        return dummy.next