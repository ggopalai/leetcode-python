# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Time Complexity - O(V)
    Space Complexity - O(1)
    """
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        # returns the total of the subtree 
        def dfs(root):
            if not root:
                return 0, 0
            
            left, left_count = dfs(root.left)
            right, right_count = dfs(root.right)

            total_at_node = left + right + root.val
            total_count = left_count + right_count + 1
            
            if (total_at_node // total_count) == root.val:
                nonlocal count
                count += 1
            
            return (left + right + root.val), (left_count + right_count + 1)

        dfs(root)

        return count