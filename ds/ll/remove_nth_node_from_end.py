#Worked, but try to optimize to one pass. 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #single node
        if head.next is None:
            return None
        
        c = 0
        t = head
        #count nodes
        while t:
            c += 1
            t = t.next
        
        #remove the head node
        if c == n:
            return head.next
        
        # -1 signifies stopping just before the node to be deleted. 
        m = c - n - 1
        t = head


        while m:
            t = t.next
            m -= 1
        
        # remove the required node. 
        t.next = t.next.next
        
        return head


#one pass
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        while n and r:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
        
        l.next = l.next.next
        
        return dummy.next
        