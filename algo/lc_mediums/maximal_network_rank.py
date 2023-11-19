class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for a, b in roads:
            adj[a].append(b)
            adj[b].append(a)
        
        mr = 0
        for i in range(n - 1):
            for j in range(i + 1, n, 1):
                cr = len(adj[i]) + len(adj[j])
                if j in adj[i]:
                    cr -= 1
                mr = max(mr, cr) 
        
        return mr

        