"""
Runtime: 60 ms, faster than 96.54% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 17.3 MB, less than 26.68% of Python3 online submissions for Remove Linked List Elements.
Worked, but looks for a more optimal solution. 
"""
def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if head is None: #empty input 
            return head
        
        while head.next and head.val == val: #initial nodes
            head = head.next
        if head is None:
            return head
        
        a = head
        
        if head.next: 
            b = head.next
        else: #single node
            if a.val == val:
                return None
            else:
                return head
        
        while b: 
            if b.val == val:
                a.next = b.next
                b = b.next
            else:
                b = b.next 
                a = a.next
            
        return head
        