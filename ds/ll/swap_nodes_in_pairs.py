# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1. My solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        f, s = head, head.next
        count = 0
        prev = f
        while s:
            #to keep track of head
            if not count:
                head = s
            
            #store the next node
            temp = s.next
            
            #swap nodes and move to next pair
            s.next = f
            f.next = temp
            f = temp
            
            #setting second node if first exists
            if not f:
                break
            else:
                s = f.next
            
            #if not, the link to the first will go away.
            if s:
                prev.next = s
                prev = f
            
            
            count += 1
                    
        return head
        
        