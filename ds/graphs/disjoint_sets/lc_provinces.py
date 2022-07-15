class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        con = dict()
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            lis = list()
            for j in range(i+1, n):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i, j)
        
        res = set()
        for i in range(len(uf.root)):
            if i == uf.root[i]:
                res.add(i)
        
        return len(res)
            
    
    
    