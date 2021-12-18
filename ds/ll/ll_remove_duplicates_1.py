def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head.next
        
        while slow and fast:
            if slow.val == fast.val:
                fast = fast.next
                slow.next = fast
            else:
                slow = fast
                fast = fast.next
        
        return head