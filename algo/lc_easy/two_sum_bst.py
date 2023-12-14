# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        d = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        
        dfs(root)

        # can also do two-pointers as input inorder gives sorted output.
        for val in nums:
            if k - val in d:
                return True
            d.append(val) 
        
        return False

        