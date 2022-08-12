class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            #if we put this condition in the end, no need of extra checks for negative numbers.
            if i[0] == '-' and len(i) > 1 or i.isdigit():
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '-':
                    stack.append(a - b)
                else:
                    #the in is to round-off division by negative powers etc
                    stack.append(int(a / b))

        return stack[-1]