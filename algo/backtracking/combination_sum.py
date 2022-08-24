class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, sub, total):
            if sum(sub) > target or i >= len(candidates):
                return
            
            if sum(sub) == target:
                res.append(sub.copy()) #doesn't work without the .copy(). but why? it should, because each function has its own sub list, right?  
                return
            
            #first decision to include the ith number
            sub.append(candidates[i])
            dfs(i, sub, total + candidates[i])
            
            sub.pop()
            dfs(i + 1, sub, total)
        
        dfs(0, [], 0)
        return res