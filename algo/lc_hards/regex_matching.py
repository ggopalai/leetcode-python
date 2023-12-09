class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(maxsize = None)
        def dfs(i, j):
            # all chars matched
            if i >= len(s) and j >= len(p):
                return True 
            
            # ran out of characters in pattern
            if j >= len(p):
                return False 
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # when there is a star after a match, we have 2 choices, either use one count of char or don't.
            if (j + 1) < len(p) and p[j + 1] == '*':
                return (dfs(i, j + 2) or (match and dfs(i + 1, j)))
            
            # char match, check next character.
            if match:
                return dfs(i + 1, j + 1)
            
            # no match found
            return False 
        
        return dfs(0, 0)

