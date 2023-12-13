class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # O(N) memory 
        stack = []
        to_remove = set()

        # evalutate character by character
        # O(N)
        for i, val in enumerate(s):
            if val.isalpha():
                continue 
            else:
                if val == '(':
                    stack.append(i) 
                else:
                    if not stack:
                        to_remove.add(i)
                        continue 
                    
                    stack.pop()
        
        # extra opening braces 
        if stack:
            for i in stack:
                to_remove.add(i)
        
        res = ""

        # reconstruct the string by ignoring invalid 
        for i, val in enumerate(s):
            if i not in to_remove:
                res += val
        
        return res


