# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        i = set()
        
        def io(root):
            if not root:
                return 
            io(root.left)
            i.add(root.val)
            io(root.right)
        
        io(root)
        l = list(i)
        l.sort()
        return l[1] if len(l) > 1 else -1