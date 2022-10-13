# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            tl = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i+1) < len(lists) else None
                tl.append(self.mergeLists(l1, l2))
            lists = tl
        
        return lists[0]
        
    
    def mergeLists(self, a, b):
        dummy = ListNode()
        t = dummy
        
        while a and b:
            if a.val < b.val:
                t.next = a
                a = a.next
            else:
                t.next = b
                b = b.next
            t = t.next
        while a:
            t.next = a
            a = a.next
            t = t.next
        while b:
            t.next = b
            b = b.next
            t = t.next
        
        return dummy.next
        
        