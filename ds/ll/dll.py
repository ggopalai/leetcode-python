class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f'Node({self.data})'

def traverseForward(head: Node):
    node = head.next
    while node:
        print(node.data)
        node = node.next

def traverseBackward(head: Node):
    node = head
    # traverse to last node
    while node.next: 
        node = node.next
    
    # traverse backward
    while node:
        print(node.data)
        node = node.prev

def addNodeRight(head:Node, node: Node) -> Node:
    a = head
    while a.next:
        a = a.next
    
    a.next = node
    node.prev = a

    return head

def addNodeLeft(head: Node, node: Node) -> Node:

    head.next.prev = node
    node.next = head.next
    head.next = node

    return head

def delRight(head: Node):

    temp = head
    while temp.next:
        temp = temp.next
    
    temp.prev.next = None

def delLeft(head: Node):
    pass

def delete(head: Node, node: Node):
    pass

if __name__ == '__main__':

    head = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    addNodeRight(head, n1)
    addNodeRight(head, n2)
    addNodeRight(head, n3)
    addNodeRight(head, n4)
    addNodeLeft(head, n5)
    delRight(head)
    addNodeRight(head, Node(6))
    traverseForward(head)
    # traverseBackward(head)
