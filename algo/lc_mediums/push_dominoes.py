class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        #convert to list as its easier to handle.
        dom = list(dominoes)
        
        #to keep track of the falling dominoes
        q = []
        for (i,d) in enumerate(dom):
            if d != ".":
                q.append((i,d))
        

        while q:
            i, d = q.pop(0)
            
            #simple case because we are processing from left to right, if we get a left first
            #dont have to check for right
            if d == 'L' and i > 0 and dom[i-1] == ".":
                q.append((i-1, 'L'))
                dom[i - 1] = "L"
            
            #need to check for left as well if we get right. 
            elif d == 'R':
                #there is a counteracting left ahead, so dont do anything.
                if i < len(dom) - 1 and dom[i+1] == ".":
                    if i < len(dom) - 2 and dom[i+2] == 'L':
                        #pop the left ahead.
                        q.pop(0)
                    else:
                        q.append((i+1, "R"))
                        dom[i+1] = 'R'
            
        
        return "".join(dom)
        