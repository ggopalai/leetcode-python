# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # pointers to manipulate the lists
        l, r, t = list1, list1, list2

        # move to end of second list 
        while t.next:
            t = t.next
        
        # one before a 
        while a - 1:
            l = l.next
            a -= 1
        
        while b:
            r = r.next
            b -= 1
        
        # switch pointers 
        l.next = list2
        t.next = r.next

        return list1
        

        