# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root and depth == 1:
            return TreeNode(val, root)

        def dfs(root, cur_depth):
            if not root:
                return
            if cur_depth == depth - 1:
                root.left = TreeNode(val, root.left)
                root.right = TreeNode(val, None, root.right)
                return
                 
            dfs(root.left, cur_depth + 1)
            dfs(root.right, cur_depth + 1)
             
        dfs(root, 1)
        
        return root