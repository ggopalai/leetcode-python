class LinkedList:
    def __init__(self) -> None:
        self.head = None

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def traverse(ll: LinkedList):
    temp = ll.head
    while temp:
        print(temp.data)
        temp = temp.next

def addNode(ll: LinkedList, n: Node) -> LinkedList:
    temp = ll.head

    while temp.next:
        temp = temp.next

    temp.next = n

    return ll


if __name__ == '__main__':

    ll = LinkedList()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    ll.head = a
    a.next = b
    b.next = c 

    traverse(ll)
    addNode(ll, Node(4))
    traverse(ll)

