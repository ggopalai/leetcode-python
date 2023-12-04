class UnionFind:
    """
    Implements disjoint set datastructure.
    Builds upon the quick union implementation by optimizing union with union ranking and find by path compression
    """

    def __init__(self, n) -> None:
        """
        Inititialize the parent and rank arrays.
        """
        self.parent = [i for i in range(n)]
        self.rank = [1] * n 
    
    def find(self, x: int) -> int:
        """
        Recursive path compression. Sets the parent of the node to its root for efficient subsequent calls.
        """
        if x == self.parent[x]:
            return x 
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 

    def union(self, x: int, y: int) -> None:
        """
        Union by ranking. Produces a more balanced tree, making the union more efficient.
        """
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty 
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1

    def connected(self, x:int, y: int):
        """
        Returns true if both the nodes have the same root. 
        """
        return self.find(x) == self.find(y)