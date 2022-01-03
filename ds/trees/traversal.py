class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None

def inorder(root):
    if root:
        inorder(root.left)
        print(f'{root.data} -> ', end='')
        inorder(root.right)

def preorder(root):
    if root:
        print(f'{root.data} -> ', end='')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(f'{root.data} -> ', end='')

if __name__ == '__main__':
   root = Node(1)
   root.left = Node(2)
   root.right = Node(3) 

   inorder(root)
   print('\n')
   preorder(root)
   print('\n')
   postorder(root)