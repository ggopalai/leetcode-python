class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        al = [[] for i in range(numCourses)]
        
        for i, j in prerequisites:
            al[i].append(j)
        
        
        order = []
        seen = set()
        def dfs(i):
            if al[i] == []:
                if i not in order:
                    order.append(i)
                return True
            if i in seen:
                return False
            
            seen.add(i)
            for x in al[i]:
                if not dfs(x):
                    return False
            seen.remove(i)
            al[i] = []
            order.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order