
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
    
        leaves = []
        # build adjacency list 
        al = [[] for _ in range(n)]
        for a, b in edges:
            al[a].append(b)
            al[b].append(a)

        # find initial leaves
        for idx, edges in enumerate(al):
            if len(edges) == 1:
                leaves.append(idx)
        
        # trim leaves
        rem_nodes = n
        while rem_nodes > 2:
            rem_nodes -= len(leaves)
            new_leaves = []

            while leaves:
                leaf = leaves.pop()
                neibor = al[leaf].pop()        
                al[neibor].remove(leaf)
            
                if len(al[neibor]) == 1:
                    new_leaves.append(neibor)
            
            leaves = new_leaves

        return leaves 