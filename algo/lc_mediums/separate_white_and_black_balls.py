# bubble sort brute force, 561/581
class Solution:
    def minimumSteps(self, s: str) -> int:
        c = 0
        s = list(s)
        for i in range(len(s)):
            for j in range(len(s) - i - 1):
                if ord(s[j + 1]) < ord(s[j]):
                    s[j + 1], s[j] = s[j], s[j + 1]
                    c += 1
        return c

# using the knowledege that we can only move 1s to the right, which means every 1 needs to be swapped with every 0 to its right
# time complexity: O(n)
class Solution:
    def minimumSteps(self, s: str) -> int:
        c = 0
        count = [0] * len(s)
        
        # space complexity: O(n) - can optimize further
        count[len(s) - 1] = 1 if s[-1] == '0' else 0
        
        # time complexity: O(n)
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                count[i] = 1 + count[i+1]
            else:
                count[i] = count[i + 1]
        
        # time complexity: O(n)
        for i in range(len(s)):
            if s[i] == '1':
                c += count[i]
        
        return c

# space optimized - only store for '1's
class Solution:
    def minimumSteps(self, s: str) -> int:
        c =  0
        from collections import defaultdict
        d = defaultdict(int)
        
        x = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                x += 1
            if s[i] == '1':
                d[i] = x
        
        for i in range(len(s)):
            if s[i] == '1':
                c += d[i]
        
        return c