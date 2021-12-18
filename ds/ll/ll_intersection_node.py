def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        if headA == headB: #single node
            return headA
        
        countA = countB = 0
        a = headA
        b = headB
        
        #count linked-list A
        while a:  
            countA += 1
            a = a.next
        
        #count linked-list B
        while b:  
            countB += 1
            b = b.next
        
        #advance pointer by difference
        a = headA
        b = headB
        if countA > countB: 
            diff = countA - countB
            while diff > 0:
                a = a.next
                diff -= 1
        elif countA < countB:
            diff = countB - countA
            while diff > 0:
                b = b.next
                diff -= 1
                    
        
        while a and b:
            if a == b:
                return a
            else:
                a = a.next
                b = b.next
        
        return None