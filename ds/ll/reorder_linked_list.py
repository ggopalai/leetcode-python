# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second part of the list
        cur, prev = slow, None
        while cur:
            tmp = cur.next
    
            cur.next = prev
            prev = cur
            cur = tmp
        
        #prev is the head of the reversed list.
        first, second = head, prev
        
        #merge the 2 parts of the list
        while second.next:
            tmp = first.next
            first.next = second
            first = tmp
            
            tmp = second.next
            second.next = first
            second = tmp
        
        return head