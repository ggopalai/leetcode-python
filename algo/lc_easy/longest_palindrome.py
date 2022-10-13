class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.defaultdict(int)
        for i in s:
            d[i] += 1
            
        ans = 0
        for v in d.values():
            #for even count, pick all. for odd, pick 1 less ( // 2 * 2 does this)
            ans += v // 2 * 2
            
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
                
        return ans

#or

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = collections.defaultdict(int)
        for i in s:
            d[i] += 1
            
        ans = 0
        for v in d.values():
            ans += v // 2 * 2    
                
        return ans if len(s) == ans else ans + 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        