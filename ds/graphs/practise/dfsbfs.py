from typing import List

def dfs_recursive(n: int, edges: List[List[int]], start: int):
    
    # create graph adjacency list
    al = [ [] for _ in range(n) ]
    for u, v in edges:
        al[u].append(v)
        al[v].append(u)
    
    # create visited set
    visited = set()

    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        print(node)

        for v in al[node]:
            dfs(v)
    
    dfs(start)

dfs_recursive(5, [[0, 1], [0, 3], [1, 2], [3, 4]], 0)

print("Iterative")

def dfs_iterative(n:int, edges: List[List[int]], start: int):
    al = [ [] for _ in range(n) ]
    for u, v in edges:
        al[u].append(v)
        al[v].append(u)
    
    visited = set()
    stack = [start]

    print(al)

    while stack:
        node = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        print(node)

        for v in al[node]:
            stack.append(v)

dfs_iterative(5, [[0, 1], [0, 3], [1, 2], [3, 4]], 0)

print("BFS")

def bfs(n:int, edges: List[List[int]], start: int):
    al = [ [] for _ in range(n) ]
    for u, v in edges:
        al[u].append(v)
        al[v].append(u)
    
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop(0)

        if node in visited:
            continue
        
        visited.add(node)
        print(node)

        for v in al[node]:
            stack.append(v)

bfs(5, [[0, 1], [0, 3], [1, 2], [3, 4]], 0)
