# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def inorder_successor(root):
            if not root.right:
                return root
            
            cur = root.right
            while cur.left:
                cur = cur.left
            return cur 
        
        def delete(root, key):
            if not root:
                return None
            
            if key < root.val:
                root.left = delete(root.left, key)
            elif key > root.val:
                root.right = delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                
                # find inorder-successor, swap value, and delete is
                in_succ = inorder_successor(root)
                root.val = in_succ.val
                root.right = delete(root.right, in_succ.val)

            return root

        return delete(root, key)