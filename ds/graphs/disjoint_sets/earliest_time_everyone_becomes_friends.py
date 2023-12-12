class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.n = n

    def find(self, x: int):
        return self.root[x]
    
    def union(self, x: int, y:int):
        rx = self.find(x)
        ry = self.find(y) 

        if rx != ry:
            for i in range(self.n):
                if self.root[i] == ry:
                    self.root[i] = rx
    
    def connected(self, x, y):
        return self.find(x) == self.find(y) 

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)
        logs.sort(key = lambda x: x[0])

        for ts, a, b in logs:
            if not uf.connected(a, b):
                uf.union(a, b)

            if len(set(uf.root)) == 1:
                return ts

        return -1
