class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        al = [[] for i in range(n)]
        # bidirectional edges
        for i, j in edges:
            al[i].append(j)
            al[j].append(i)
        
        seen = set()
        s = [0]
        while s:
            a = s.pop()
            #cycle condition
            if a in seen:
                return False
            
            seen.add(a)
            
            for i in al[a]:
                if i not in seen:
                    s.append(i)
        
        # checking for disconnected components 
        return True if len(seen) == n else False
