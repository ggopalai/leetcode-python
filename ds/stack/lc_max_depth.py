def maxDepth(self, s: str) -> int:
        res = 0
        stack = list()
        for i in s:
            if i == '(':
                stack.append(i)
                if len(stack) > res:
                    res = len(stack)
            elif i == ')':
                stack.pop()
        
        return res