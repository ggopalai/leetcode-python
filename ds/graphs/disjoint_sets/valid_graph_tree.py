class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        class UnionFind:
            def __init__(self, n):
                self.parent = [i for i in range(n)] 
            
            def find(self, x):
                return self.parent[x]
            
            def union(self, x, y):
                rx = self.find(x)
                ry = self.find(y) 
                
                if rx != ry:
                    for i in range(n):
                        if self.parent[i] == ry:
                            self.parent[i] = rx
            
        # for a graph to be a valid tree, number of edges is n - 1
        if len(edges) != (n - 1):
            return False

        # case 2, all nodes must be connected, apply a union on all the 
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y) 
        
        return True if len(set(uf.parent)) == 1 else False

