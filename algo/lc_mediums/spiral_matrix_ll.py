class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]

        l, t = 0, 0
        r, b = n, n
        cur = 1

        while l < r and t < b:
            
            i = l
            while i < r:
                res[t][i] = cur
                cur += 1
                i += 1
            t += 1

            j = t
            while j < b:
                res[j][r - 1] = cur
                cur += 1
                j += 1
            r -= 1

            i = r - 1
            while i >= l:
                res[b - 1][i] = cur
                cur += 1
                i -= 1
            b -= 1

            j = b - 1
            while j >= t:
                res[j][l] = cur
                cur += 1
                j -= 1
            l += 1

        return res