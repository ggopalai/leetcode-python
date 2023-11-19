class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        
        i = 0
        while i < l1 and i < l2 and i < l3 and s1[i] == s2[i] and s1[i] == s3[i]:
            i += 1
        
        if i < 1:
            return -1
        
        return l1 - i + l2 - i + l3 - i
        