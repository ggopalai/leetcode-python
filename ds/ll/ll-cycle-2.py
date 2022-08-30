
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. Linear time and linear space solution
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        seen = set()
        
        while t:
            if t not in seen:
                seen.add(t)
                t = t.next
            else:
                return t
        
        return None

# 2. Linear and Constant Space - Floyd's Hare and Tortoise algo (try to understand the math proof)
        