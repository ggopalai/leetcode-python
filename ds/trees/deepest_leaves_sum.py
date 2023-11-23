# pre-compute + dfs
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def max_depth(root, depth):
            if not root:
                return depth - 1
            return max(max_depth(root.left, depth + 1), max_depth(root.right, depth + 1))
        
        md = max_depth(root, 0)
        
        res = 0
        def dfs(root, depth):
            if not root:
                return 
            if depth == md:
                nonlocal res
                res += root.val
                return
            dfs(root.right, depth + 1)
            dfs(root.left, depth + 1)
        
        dfs(root, 0)

        return res

# bfs 
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = [(root, 0)]
        res, md = 0, 0
        
        while q:
            node, depth = q.pop(0)
            # leaf
            if not node.left and not node.right:
                # new max depth, reset sum
                if depth > md:
                    md = depth
                    res = 0
                res += node.val
            else:
                if node.left:
                    q.append((node.left, depth + 1))
                if node.right:
                    q.append((node.right, depth + 1))
        
        return res


          

        