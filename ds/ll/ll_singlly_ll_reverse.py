# Iterative
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        
        previous = None
        current = head
        following = current.next
        
        while current:
            current.next = previous
            previous = current
            current = following
            if following:
                following = following.next
                
        head = previous 
        
        return head

# Recursive solution - 
