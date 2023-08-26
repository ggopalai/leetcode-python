# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 1. My solution 

import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        l = 1
        q = [(root, l)] #[(node, 1)]
        r = []
        d = collections.defaultdict(list)
        while q:
            c, l = q.pop(0)
            
            if not c:
                continue
            d[l].append(c.val) #dict to keep track of level
            
            q.append((c.left, l+1))
            q.append((c.right, l+1))
                    
        for n in d.values():
            r.append(n)
        
        return r

# BFS with queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        res = []
        def bfs(root):
            nonlocal res
            q = [root]
            res = []

            while q:
                t = []
                level_num = len(q)

                for _ in range(level_num):
                    node = q.pop(0)
                    t.append(node.val)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                res.append(t)

        bfs(root)

        return res            