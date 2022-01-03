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

if __name__ == '__main__':
   root = Node(10)
   root.left = Node(9)
   root.right = Node(11) 
   root.left.left = Node(5)
   root.left.right = Node(9.5)
   print(search(root, 9))
