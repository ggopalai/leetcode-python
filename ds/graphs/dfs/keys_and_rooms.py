class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        stack = [0]

        # traverse
        while stack:
            cur = stack.pop()
            
            # avoid infinte loop
            if cur in visited:
                continue
            
            # mark visited
            visited.add(cur)

            for keys in rooms[cur]:
                stack.append(keys)
        
        return True if len(visited) == len(rooms) else False

        