# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # dummy node to handle edge cases
        # handles cases with reversing starts from first position
        dummy = ListNode(0, head)

        # find prev node before the reversing begins
        leftPrev, cur = dummy, head
        for _ in range(left - 1):
            leftPrev, cur = cur, cur.next

        # reverse the required nodes
        prev = None
        for _ in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # correct the order of all the nodes
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next


