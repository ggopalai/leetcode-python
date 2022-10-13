class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        count = 0
        i = 0
        while i < len(s):
            if s[i] == 'I' and i < len(s) - 1:
                if s[i+1] in ['V', 'X']:
                    count += d[s[i+1]] - 1
                    i += 2
                    continue
            elif s[i] == 'X' and i < len(s) - 1:
                if s[i+1] in ['L', 'C']:
                    count += d[s[i+1]] - 10
                    i += 2
                    continue
            elif s[i] == 'C' and i < len(s) - 1:
                if s[i+1] in ['D', 'M']:
                    count += d[s[i+1]] - 100
                    i += 2
                    continue
            count += d[s[i]]
            i += 1
        return count

# 2. LC
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        count = 0
        i = 0
        while i < len(s):
            #because we always right big to small. only exceptions are the paired subtractive cases. 
            if i < len(s) - 1 and d[s[i]] < d[s[i+1]]:
                count += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                count += d[s[i]]
                i += 1
        return count 