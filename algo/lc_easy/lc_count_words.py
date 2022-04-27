# leetcode.com/problems/count-common-words-with-one-occurrence/

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a = dict()
        b = dict()
        
        for i in words1:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        
        for i in words2:
            if i not in b:
                b[i] = 1
            else:
                b[i] += 1
                
        count = 0
        
        for i in words1:
            if i in a and i in b and a[i] == 1 and b[i] == 1:
                count += 1
        
        return count