"""
Time - O(N)
Space - O(N)
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        ob = []
        ast = []

        for idx, c in enumerate(s):
            if c == '(':
                ob.append(idx)
            elif c == '*':
                ast.append(idx)
            else:
                if ob:
                    ob.pop()
                elif ast:
                    ast.pop()
                else:
                    return False 
        
        if ob and not ast or len(ob) > len(ast):
            return False 
        
        while ob:
            if ob[-1] > ast[-1]:
                return False 
            ob.pop()
            ast.pop()
        
        return True 
            
