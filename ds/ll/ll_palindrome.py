# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  #wasn't very optimized. think of another solution. Runtime: 916 ms, faster than 31.39% of Python3 online submissions for Palindrome Linked List.
# Memory Usage: 47.6 MB, less than 9.34% of Python3 online submissions for Palindrome Linked List.
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head.next is None:
            return True
        
        st = ''
        a = head
        while a:
            st = st + str(a.val)
            a = a.next
        
        b = "".join(reversed(st))
        if b == st:
            return True 
    
        return False
        
