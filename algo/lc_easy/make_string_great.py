# iterative, quadratic, constant space 
class Solution:
    def makeGood(self, s: str) -> str:
        while len(s) > 1:
            find = False 

            for i in range(len(s) - 1):
                cur, nc = s[i], s[i + 1] 
                if abs(ord(cur) - ord(nc)) == 32:
                    s = s[:i] + s[i+2:] 
                    find = True
                    break
            
            if not find:
                break
        
        return s

#iteractive, linear time and space
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)


