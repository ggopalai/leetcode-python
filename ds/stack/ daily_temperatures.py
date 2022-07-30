class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = [(temperatures[0], 0)]
        
        for i in range(1, len(temperatures)):
            if temperatures[i] > s[-1][0]:
                while s and temperatures[i] > s[-1][0]:
                    _, b = s.pop()
                    res[b] = i - b
                s.append((temperatures[i], i))
            else:
                s.append((temperatures[i], i))
        
        return res
        
        
        