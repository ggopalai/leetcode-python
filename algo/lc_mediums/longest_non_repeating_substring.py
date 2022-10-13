class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0

        #keep track of visited characters
        charSet = set()
        
        #loop to keep changing right pointer
        for r in range(len(s)):
            #if we encounter a char which was already there, remove the left most char.
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            count = max(count, r - l + 1)
        
        return count 