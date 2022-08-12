# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ts = [False]
        
        def path(root, cs):
            if not root:
                return            
            if (cs + root.val) == targetSum and (not root.right and not root.left):
                ts[0] = True
                return
            else:
                path(root.left, cs + root.val)
                path(root.right, cs + root.val)
                
        path(root, 0)    
        return ts[0]