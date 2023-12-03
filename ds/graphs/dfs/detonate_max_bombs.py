class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # build graph
        n = len(bombs)
        al = [[] for _ in range(n)]
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                dist = math.sqrt(math.pow(bombs[i][0] - bombs[j][0], 2) + math.pow(bombs[i][1] - bombs[j][1], 2))
                if dist <= bombs[i][2]:
                    al[i].append(j)
                if dist <= bombs[j][2]:
                    al[j].append(i)
        
        # track all detonated bombs
        def dfs(node, visited):
            visited.add(node)

            for i in al[node]:
                if i not in visited:
                    dfs(i, visited)
            
            return len(visited)
            
        # run dfs on every bomb
        res = 1
        for i in range(n):
            visited = set()
            res = max(res, dfs(i, visited))
            
        return res