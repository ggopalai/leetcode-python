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

# used to find the inorder successor for the right subtree. 
def minNodeValue(root: Node) -> Node:
    cur = root

    while cur.left:
        cur = cur.left

    return cur

def delete(root:Node, key:int) -> Node:
    if not root:
        return root
    
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if not root.left and not root.right: #leaf-node
            return None
        elif not root.left and root.right: #single child
            return root.right
        elif not root.right and root.left:
            return root.left
        else: #has both children
            temp = minNodeValue(root.right)
            root.data = temp.data
            root.right = delete(root.right, root.data)

    return root



if __name__ == '__main__':
   hroot = Node(50)
   root = insert(hroot, Node(25))
   root = insert(hroot, Node(100))
   root = insert(hroot, Node(125))
   root = insert(hroot, Node(70))
   inorder(root)
   root = delete(root, 100)
   print('\n')
   inorder(root)
