class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None


def search(root, key):
    if root is None:
        return 
    if root.data == key:
        return root.data
    elif root.data < key:
        return search(root.right, key)
    else:
        return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(f'{root.data} -> ', end='')
        inorder(root.right)

def insert(root: Node, node: Node) -> Node:
    if not root:
        return node
    
    if node.data < root.data:
        root.left = insert(root.left, node)
    elif node.data > root.data:
        root.right = insert(root.right, node)

    return root

if __name__ == '__main__':
   hroot = Node(50)
   root = insert(hroot, Node(25))
   root = insert(hroot, Node(100))
   root = insert(hroot, Node(75))
   root = insert(hroot, Node(30))
   inorder(root)
