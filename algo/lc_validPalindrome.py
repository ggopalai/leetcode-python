# https://leetcode.com/problems/valid-palindrome/

# Runtime: 72 ms, faster than 29.20% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.7 MB, less than 60.82% of Python3 online submissions for Valid Palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = str()
        
        for i in s:
            if i.isalnum():
                temp += i.lower()
                
        if temp[::-1] == temp:
            return True
    
        return False
        