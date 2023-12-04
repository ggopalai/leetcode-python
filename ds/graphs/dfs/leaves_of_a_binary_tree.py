# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Time - O(n log n)
    Can reduce to n if we can directly place the values the correct position.
    """
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        h = defaultdict(list)
        
        # O(V)
        def dfs(root):
            if not root:
                return -1
            
            height = 1 + max(dfs(root.left), dfs(root.right))
            h[height].append(root.val)
            
            return height
        
        # build height dictionary
        dfs(root)

        # O(h log h) or n log n for skewed tree
        temp = [(k, v) for k, v in h.items()].sort()

        return [v for (_ ,v) in temp]

# linear solution
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        res = [[] for _ in range(100)]

        def dfs(root):
            if not root:
                return -1
            
            height = 1 + max(dfs(root.left), dfs(root.right))
            res[height].append(root.val)
            
            return height
        
        # build height dictionary
        dfs(root)

        temp = [v for v in res if v]

        return temp

        


        
        