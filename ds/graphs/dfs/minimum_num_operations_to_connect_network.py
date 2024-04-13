class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        seen = set()
        adj = [[] for _ in range(n)]
        for a, v in connections:
            adj[a].append(v)
            adj[v].append(a)
        count = 0
        
        def dfs(n):
            if n in seen:
                return 
            seen.add(n)
            for nei in adj[n]:
                if nei not in seen:
                    dfs(nei)
        
        for i in range(n):
            if i not in seen:
                dfs(i)
                count += 1
        
        return count - 1

