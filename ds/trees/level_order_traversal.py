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

# 2. Neetcode solution without using a dict.
            