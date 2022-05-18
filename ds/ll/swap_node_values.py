# Read the question wrong. No need to swap the nodes, just swap the values. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#This swaps nodes. Need to swap values only.
class Solution:
    def addNode(self, head: ListNode, n: ListNode) -> ListNode:
            temp = head
            while temp.next:
                temp = temp.next
            
            temp.next = n
            return head
        
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = list()
        t = head
        
        #converting linked-list to an array
        while t:
            nodes.append(ListNode(val=t.val))
            t = t.next
                
        #swap the nodes
        nodes[k-1], nodes[-k] = nodes[-k], nodes[k-1]

        
        res = nodes[0]
        #reconstruct the linked-last
        for i in range(1, len(nodes)):
            res = self.addNode(res, nodes[i])
        
        return res
    
    
#3-pass solution 

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t = head
        #number of nodes
        count = 0
        while t:
            count += 1
            t = t.next
        
        #set front pointer
        fNode = head
        i = k-1
        while i > 0:
            fNode = fNode.next
            i -= 1
        
        #set end pointer
        eNode = head
        i = count - k
        while i > 0:
            eNode = eNode.next
            i -= 1
        
        #swap values
        fNode.val, eNode.val = eNode.val,fNode.val
        
        return head

# 2-pass solution - front node can be found out while counting itself. 

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t = head
        fNode = head
        count = 0
        while t:
            count += 1
            t = t.next
            if count == k-1:
                fNode = t
        
        eNode = head
        i = count - k
        while i > 0:
            eNode = eNode.next
            i -= 1
        
        fNode.val, eNode.val = eNode.val,fNode.val
        
        return head

# 1-pass - the k distance is the same from start and end. so using start difference, find the end difference. 
class Solution:    
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        t = head
        fNode = head
        eNode = head
        count = 0
        while t.next:
            count += 1
            if eNode:
                eNode = eNode.next
            t = t.next
            if count == k-1:
                fNode = t
                eNode = head
            
        
        fNode.val, eNode.val = eNode.val,fNode.val
        
        return head