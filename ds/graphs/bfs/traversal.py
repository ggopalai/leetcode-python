from typing import List

def bfsIterative(n: int, edges: List[List[int]], start: int):

    q = [start]
    
    al = [ [] for _ in range(n)]
    for a, b in edges:
        al[a].append(b)
        al[b].append(a)
    seen = set()

    while q:
        node = q.pop(0)

        if node in seen:
            continue
        print(f"{node}->")
        seen.add(node)

        for i in al[node]:
            q.append(i)
    

bfsIterative(6, [ [0,1], [0,4], [1,2], [1,3], [4,5] ], 0)

