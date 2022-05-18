# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next is None:
            return head
        
        count = 0
        a = head
        while a:
            count += 1
            a = a.next
            
        if count % 2 == 0:
            mid = count/2 + 1
        else:
            mid = count//2 + 1 # second node if even number of nodes
            
        a = head
        count = 1
        while count < mid:
            a = a.next
            count += 1
        
        return a 
        

# try solving using 2 pointers
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow