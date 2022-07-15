from typing import List, Set


def dfsIterative(n: int, edges: List[ List[ int ] ], start: int):
    seen = set()
    stack = [start]
    al = [ [] for _ in range(n) ]
    for a, b in edges:
        al[a].append(b)
        al[b].append(a)
    
    while stack:
        node = stack.pop()

        if node in seen:
            continue
        print(f"{node}->")
        seen.add(node)

        for i in al[node]:
            stack.append(i)

dfsIterative(6, [ [0, 4], [0, 1], [1, 3], [1, 2],  ], 0)

print("Recursive")

def dfsRescursive(al: List[List[int]], seen: Set, node):

    if node in seen:
        return 
    seen.add(node)

    print(node)

    for i in al[node]:
        dfsRescursive(al, seen, i)

dfsRescursive([[1, 4], [0, 2, 3], [1], [1], [0]], set(), 0)

# If using recursive method on a DAG, no need to maintain a visited/seen set.