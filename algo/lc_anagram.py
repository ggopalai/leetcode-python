 from collections import Counter 
 
 def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        dic = dict()
        
        for i in s:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1
        
        for i in t:
            if i not in dic.keys():
                return False
            else:
                dic[i] = dic[i] - 1
        
        v = dic.values()
        for i in v:
            if i > 0:
                return False
            
        
        return True

# Much faster
def isAnagramCounter(self, s: str, t: str) -> bool:
        
        if Counter(s) == Counter(t):
            return True
        
        return False