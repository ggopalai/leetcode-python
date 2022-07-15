from typing import List

#dfs solution
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end = len(graph) - 1
        
        def dfs(node, path):
            if node == end:
                output.append(path)
            
            for i in graph[node]:
                dfs(i, path + [i])
            
        
        output = []
        dfs(0, [0])
        return output


#bfs solution
