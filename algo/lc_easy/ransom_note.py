class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        
        hmap = collections.defaultdict(int)
        
        for i in ransomNote:
            hmap[i] += 1
        
        for i in magazine:
            hmap[i] -= 1
        
        for i in hmap.values():
            if i > 0:
                return False
        
        return True
            