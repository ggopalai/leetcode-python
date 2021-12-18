"""
Implemented this with a custom Stack class build around a List. Try implementing in List.  
"""
class Stack:
    
    def __init__(self):
        self.stack = list()
    
    def push(self, n: str):
        self.stack.append(n)
    
    def pop(self) -> str:
        if len(self.stack) == 0:
            return None
        last = self.stack[-1]
        self.stack.pop()
        return last
    
    def length(self) -> int:
        return len(self.stack)
        
        
class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        
        for i in s:
            if i in ['{', '(', '[']:
                stack.push(i)
            elif i == '}':
                p = stack.pop()
                if p != '{' or p == None:
                    return False
            elif i == ')':
                p = stack.pop()
                if p != '(' or p == None:
                    return False
            elif i == ']':
                p = stack.pop()
                if p != '[' or p == None:
                    return False
        
        if stack.length() > 0:
            return False
        
        return True