#1. Neetcode solution. Uses 2 helper functions, one hashmap and a double linked list, left and right dummy nodes. 
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left
    
    #remove node
    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
    
    #insert node at MRU position
    def insert(self, node):
        p = self.right.prev
        p.next = self.right.prev = node
        node.next, node.prev = self.right, p

    def get(self, key: int) -> int:
        if key in self.cache:
            #move node to MRU position
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return self.cache[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #remove the node and insert new node at MRU.
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        
        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#didnt work, got stuck in an infinite loop inside getnode.
class Node:
    def __init__(self, key, val, nex = None, prev = None):
        self.val = (key, val)
        self.next = nex
        self.prev = prev
        
class LinkedList:
    def __init__(self, capacity = 0, head = None):
        self.capacity = capacity
        self.head = head
        self.count = 0
    
    def addNode(self, key, val):
        self.count += 1
        
        if not self.head:
            return Node(key, val)
        
        newNode = Node(key, val)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        
        if self.count > self.capacity:
            t, prev = self.head, None
            while t.next:
                prev = t
                t = t.next
            prev.next = None
        
        print(self.head.val)
        return self.head
    
    def getNode(self, key):
        if not self.head:
            return -1
        t, p = self.head, None
        res = -1
        while t:
            if t.val[0] == key:
                if not p:
                    return t.val[1]
                
                res = t.val[1]
                
                p.next = t.next
                if t.next:
                    t.next.prev = p
                
                t.next = self.head
                t.prev = None
                
                self.head.prev = t
                self.head = t
            else:
                p = t
                t = t.next
        
        return res
        
class LRUCache:
    def __init__(self, capacity: int):
        self.ll = LinkedList(capacity)

    def get(self, key: int) -> int:
        return self.ll.getNode(key)
        
    def put(self, key: int, value: int) -> None:
        self.ll.head = self.ll.addNode(key, value)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)