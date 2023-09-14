# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        from collections import defaultdict

        # count number of occurrences in first pass
        c = defaultdict(int)
        t = head
        while t:
            c[t.val] += 1
            t = t.next

        toDel = set()
        for k, v in c.items():
            if v > 1:
                toDel.add(k)
        
        # dummy node to handle edge case of deleting head
        dummy = ListNode(0, head)
        
         # second pass to delete
        t = dummy
        while t and t.next:
            while t.next and t.next.val in toDel:
                t.next = t.next.next
            t = t.next

        return dummy.next

        
        