class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # build graph and indegree array
        al = [[] for _ in range(n)]
        from collections import defaultdict
        
        indegree = [0] * n

        for s, d in relations:
            al[s-1].append(d-1)
            indegree[d-1] += 1
        
        free_nodes = []
        for idx, val in enumerate(indegree):
            if val == 0:
                free_nodes.append(idx)
        
        sems = []

        # top sort, keep track of number of iterations 
        while free_nodes:
            n = len(free_nodes)
            sems.append(n)

            for _ in range(n):
                node = free_nodes.pop(0)
                for nei in al[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        free_nodes.append(nei)
    
        return len(sems) if not sum(indegree) else -1






        