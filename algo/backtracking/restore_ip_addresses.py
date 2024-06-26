class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        # invalid ip length
        if len(s) > 12 or len(s) < 4:
            return res
        
        # i - current index 
        # dots - the number of dots added so far 
        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return 
            if dots > 4:
                return
            # min - handles out of bounds 
            for j in range(i, min(i + 3, len(s))):
                # valid numbers and leading 0s     
                if int(s[i:j+1]) <= 255 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, curIP + s[i:j+1] + ".")
        
        backtrack(0, 0, "") 
        return res