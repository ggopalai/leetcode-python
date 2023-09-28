class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(cur, i):
            if len(cur) == len(s):
                res.append(cur)
                return
            if s[i].isalpha():
                dfs(cur + s[i].lower(), i + 1)
                dfs(cur + s[i].upper(), i + 1)
            else:
                dfs(cur + s[i], i + 1)

        dfs("", 0)
        return res
        