class Solution:
    def countHomogenous(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[l] == s[r]:
                r += 1
            else:
                res += (r - l) * (r - l + 1) // 2
                l = r
        res += (r - l) * (r - l + 1) // 2

        return int(res % (10**9 + 7))



