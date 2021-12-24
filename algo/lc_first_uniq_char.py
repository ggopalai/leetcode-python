"""
https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
"""

def firstUniqChar(self, s: str) -> int:
        d = dict()
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
            
        for i in d.keys():
            if d[i] == 1:
                return s.index(i)
        
        return -1

"""
Follow this up with a queue solution? 
"""