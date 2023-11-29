class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # can be solved using top sort 
        indegree = [0] * numCourses

        # build adjacency list and indegree array
        al = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            al[b].append(a)
            indegree[a] += 1

        # queue to track independent nodes
        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # apply top sort
        order = []
        while q:
            node = q.pop(0)
            
            # add to ordering
            order.append(node)

            for nei in al[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(order) != numCourses:
            return []
        
        return order


        