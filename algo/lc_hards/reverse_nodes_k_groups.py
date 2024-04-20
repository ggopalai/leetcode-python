# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        # kth node to reverse  
        def get_kth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        # groupNext -> starting node of the next group 
        # groupPrev -> node before the group 
        while True:
            kth = get_kth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next

            # normal reversal
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr 
                curr = tmp
            
            # kth is the new first node of the reversed group
            # groupPrev.next is the last node of the reversed group 
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next

        
        

