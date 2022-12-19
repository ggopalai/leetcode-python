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

# constant space solution
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next: return True
        t = head
        
        count = 0
        while t:
            count += 1
            t = t.next
        s = f = head

        while f and f.next:
            s = s.next
            f = f.next.next
        if count % 2 == 1:
            s = s.next
        
        #reverse linked list
        def reverse(node):
            p = None
            c = node

            while c:
                tmp = c.next
                c.next = p
                p = c
                c = tmp
            return p
        sh = reverse(s)
        
        t = head 
        while sh:
            if t.val != sh.val:
                return False
            t = t.next
            sh = sh.next
        
        return True 
        
