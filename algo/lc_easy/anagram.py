'''
ord(char) -> gives ascii value of character
chr(int) -> gives the char of the ascii (number)
'''

import sys 

def anagram(s: str, r: str) -> bool:
    l = []
    for i in range(150):
        l.append(0)
    
    if s == r:
        return True
    if len(s) != len(r):
        return False

    for i in range(0, len(s)):
        l[ord(s[i])] = l[ord(s[i])] + 1
        l[ord(r[i])] = l[ord(r[i])] - 1
    
    for i in l:
        if i > 0:
            return False
    
    return True

if __name__ == '__main__':
    print(anagram(sys.argv[1], sys.argv[2]))

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = [0] * 26
        for i in range(len(s)):
            d[ord(s[i])-97] += 1
            d[ord(t[i])-97] -= 1
        
        for i in d:
            if i != 0:
                return False
        
        return True

#dictionary solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in t:
            if i in d:
                d[i] -= 1
            else:
                d[i] = -1
        
        vals = d.values()
        for i in vals:
            if i != 0:
                return False
            