# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        one = list()
        two = list()
    
        def pushToList(root, l):
            if not root:
                l.append(None)
                return root
            l.append(root.val)
            pushToList(root.left, l)
            pushToList(root.right, l)
         
        
        pushToList(p, one)
        pushToList(q, two)
        
        if one == two:
            return True
        
        return False