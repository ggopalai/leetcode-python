class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inc = [[] for _ in range(n)]
        
        for a, b in edges:
            inc[b].append(a)
        
        c = []
        for i in range(n):
            if not inc[i]:
                c.append(i)
        
        return c