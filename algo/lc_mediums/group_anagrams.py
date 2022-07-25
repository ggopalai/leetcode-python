import collections 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = collections.defaultdict(list)
        
        for i in strs:
            val = [0] * 26
            for j in i:
                val[ord(j) - 97] += 1
            
            dt = tuple(val)
            d[dt].append(i)
        
        res = []
        for i in d.values():
            res.append(i)
        
        return res
        
            
        
        