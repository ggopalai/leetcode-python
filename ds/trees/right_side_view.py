# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        l = 1
        q = [(root, l)]
        d = collections.defaultdict(list)
        
        while q:
            c, l = q.pop(0)
            if not c:
                continue
            d[l].append(c.val)
            
            q.append((c.left, l+1))
            q.append((c.right, l+1))
            
        res = []
        for i in d.values():
            res.append(i[-1])
        
        return res
            
            
            
            
            