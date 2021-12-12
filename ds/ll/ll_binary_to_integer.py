# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        if head.next is None:
            return head.val
        
        count = 0
        a = head
        ll = []
        while a:
            count += 1
            ll.append(a.val)
            a = a.next

        res = 0
        for i in ll:
            count -= 1
            res = res + (i * 2**(count))
            
        return res
            
        