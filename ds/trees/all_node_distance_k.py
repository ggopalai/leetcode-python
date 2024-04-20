# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        res = []

        def build_graph(cur, parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left, cur)
            if cur.right:
                build_graph(cur.right, cur)
        build_graph(root, None)

        queue = [(target.val, 0)]
        seen = set()

        while queue:
            node, dist = queue.pop(0)
            seen.add(node)

            if dist == k:
                res.append(node)
                continue
            
            for nei in graph[node]:
                if nei not in seen:
                    queue.append((nei, dist + 1))

        return res
        
