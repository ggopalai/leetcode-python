# https://leetcode.com/problems/unique-number-of-occurrences/
def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict()
        
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        if len(d.values()) == len(set(d.values())):
            return True
        
        return False

