# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # return 2 values - max when robbing this node and max when not robbing
        def dfs(node):
            if not node:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            # if robbing, cannot rob children
            rob = node.val + left[1] + right[1]

            # if not robbing, may or may not rob children, hence max of both
            not_rob = max(left) + max(right)

            return [rob, not_rob]
        
        return max(dfs(root))