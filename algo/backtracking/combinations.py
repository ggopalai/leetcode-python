class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        # keep track of current combination and index
        def dfs(cur, i):
            # base cases
            if len(cur) == k:
                t = cur.copy()
                res.append(t)
                return
            if i == n + 1:
                return 
            
            # either include or exclude current number
            dfs(cur + [i], i + 1)
            dfs(cur, i + 1)
        
        dfs([], 1)

        return res
        