from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        #store the last occurrence of each character
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] = i
                
        l, end = 0, d[s[0]]
        res = []
        for i in range(len(s)):
            cur_end = d[s[i]]
            end = max(end, cur_end)
            # size of the current partition 
            l += 1
            
            # here we know that none of the previous characters will occur later on. 
            if i == end:
                res.append(l)
                l = 0
        
        return res
            
        