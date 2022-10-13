class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def bt(openC, closedC):
            
            #we've reached an valid permutation of ()
            if openC == closedC == n:
                res.append("".join(stack)) 
            
            #first check if we can add '('
            if openC < n:
                stack.append("(")
                bt(openC + 1, closedC)
                stack.pop()
            
            #then check if '(' can be added
            if closedC < openC:
                stack.append(")")
                bt(openC, closedC + 1)
                stack.pop()
        
        bt(0, 0)
        return res