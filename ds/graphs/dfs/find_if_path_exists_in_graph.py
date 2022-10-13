#dfs solution.
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        #supporting ds - stack[], adjacency list [[]], seen {}
        
        stack = [source]
        
        #an adjacency list to keep track of neighbours
        al = [[] for _ in range(n)]
        for a, b in edges:
            al[a].append(b)
            al[b].append(a)
            
        #set to track visited nodes
        seen = set()
        
        while stack:
            
            #current node 
            node = stack.pop()
            
            #reached destination
            if node == destination:
                return True
            
            #keep track of seen nodes
            if node in seen:
                continue
            seen.add(node)
            
            #add all neighbours for dfs
            for n in al[node]:
                stack.append(n)
        
        return False

#disjoint set solution - 