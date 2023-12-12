# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        # faster lookups
        del_set = set(to_delete)
        res = []

        # post order dfs
        def dfs(root):
            # base case 
            if not root:
                return None
            
            # check children first (postorder)
            root.left = dfs(root.left)
            root.right = dfs(root.right)

            # crux, if node is to be deleted, manage children if they exist.
            if root.val in del_set:
                if root.left:
                    res.append(root.left)
                if root.right:
                    res.append(root.right)
                return None
            
            return root

        # check root
        node = dfs(root)
        if node:
            res.append(node) 

        return res 