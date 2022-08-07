class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, sub, total):
            if sum(sub) > target or i >= len(candidates):
                return
            
            if sum(sub) == target:
                res.append(sub.copy())
                return
            
            sub.append(candidates[i])
            dfs(i, sub, total + candidates[i])
            
            sub.pop()
            dfs(i + 1, sub, total)
        
        dfs(0, [], 0)
        return res