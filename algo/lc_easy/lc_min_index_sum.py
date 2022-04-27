# https://leetcode.com/problems/minimum-index-sum-of-two-lists

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = dict()
        
        for i in list1:
            if i in list2:
                d[i] = list1.index(i) + list2.index(i)
                
        a = min(d.values())
        res = list()
        for i in d:
            if d[i] == a:
                res.append(i)
        
        return res
        