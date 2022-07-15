class QuickFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    def find(self, x: int) -> int:
        return self.root[x]

    def union(self, x: int, y: int):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


uf = QuickFind(10)

uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)

print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
print(uf.root)

uf.union(4, 9)
print(uf.connected(4, 9))  # true
print(uf.root)