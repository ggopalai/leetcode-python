"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #maintain mapping between old and copied nodes.
        oldToNew = {}
        
        def dfs(node):
            #if copy is already created, return copy.
            if node in oldToNew:
                return oldToNew[node]
            
            #else, create copy. set val, populate map.
            copy = Node(node.val)
            oldToNew[node] = copy
            
            #populate neighbors for copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            #return the created copy
            return copy
        
        return dfs(node) if node else None
        
        