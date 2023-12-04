
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        dia = 0

        def dfs(root):
            if not root:
                return 0
            
            curDia = 0
            maxDepth = []
            toReturn = 0
            
            for i in root.children:
                md = dfs(i)
                maxDepth.append(md)
            
            nonlocal dia
            if maxDepth: 
                if len(maxDepth) <= 2:
                    curDia = sum(maxDepth)
                else:
                    maxDepth.sort(reverse=True)
                    curDia = sum(maxDepth[:2])

                toReturn = max(maxDepth)
                
            dia = max(curDia, dia)
            
            return toReturn + 1

        dfs(root)

        return dia