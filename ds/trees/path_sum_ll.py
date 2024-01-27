# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(root, cur):
            if not root:
                return 
            cur = cur + [root.val] 
            if sum(cur) == targetSum and (not root.left and not root.right):
                res.append(cur + [])

            dfs(root.left, cur)
            dfs(root.right, cur)
            
        dfs(root, [])

        return res