class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        al = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            al[i].append(j)
            
        seen = set()
        def dfs(i):
            #base cases
            if i in seen:
                return False
            if al[i] == []:
                return True
            
            #add and remove as we're using a common set. 
            seen.add(i)
            for a in al[i]:
                if not dfs(a):
                    return False
            seen.remove(i)
            
            #this is to eliminate repeated work. once we know node is fine from a indirect call, 
            # dont have to again for direct call. 
            al[i] = []
            
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True

#didnt work as numbers were staying in set even though set() was called for each node.
# al = [[] for _ in range(numCourses)]
#         for i, j in prerequisites:
#             al[i].append(j)
            
#         cycle = True
#         def dfs(i, seen):
#             if i in seen:
#                 print(i, seen)
#                 nonlocal cycle
#                 cycle = False
            
#             seen.add(i)
#             for a in al[i]:
#                 dfs(a, seen)
        
#         for i in range(numCourses):
#             dfs(i, set())

#         return cycle
        
            
            