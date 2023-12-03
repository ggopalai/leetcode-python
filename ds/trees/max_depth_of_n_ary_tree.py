"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# dfs
class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def dfs(root):
            if not root:
                return 0
            
            md = []
            for c in root.children:
                md.append(dfs(c))
            
            return max(md) + 1 if md else 1
        
        return dfs(root)

      
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # bfs 

        if not root:
            return 0
        
        md = 1
        q = [(root, 1)]

        while q:
            node, depth = q.pop(0)

            md = max(md, depth)

            for c in node.children:
                q.append((c, depth + 1))
        
        return md