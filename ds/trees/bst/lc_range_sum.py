# https://leetcode.com/problems/range-sum-of-bst/

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val <= high and root.val >= low:
            return root.val + self.rangeSumBST(root.left, low, high) +  self.rangeSumBST(root.right, low, high)
        else:
            return self.rangeSumBST(root.left, low, high) +  self.rangeSumBST(root.right, low, high)
        
