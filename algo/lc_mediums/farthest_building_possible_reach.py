# 1. Naive solution with choosing bricks first. passed 58/77 test cases. 
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i = 0
        while bricks or ladders:
            if i == len(heights) - 1:
                break
            if heights[i] >= heights[i+1]:
                i += 1
            else:
                diff = heights[i+1] - heights[i]
                if diff <= bricks:
                    bricks -= diff
                    i += 1
                elif ladders:
                    ladders -= 1
                    i += 1
                else:
                    return i
        
        return i

#. Naive with ladder first over bricks. - 67/77 passed. 

# 3. Accepted. Min heap approach. 
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lh = []
        heapq.heapify(lh)
        for i in range(len(heights) - 1):
            if heights[i+1] - heights[i] <= 0:
                continue
            climb = heights[i + 1] - heights[i]

            #use up all the ladders first
            if ladders:
                heapq.heappush(lh, climb)
                ladders -= 1
            #after using up ladders
            else:
                # 0 ladders or if smaller climb
                if not lh or climb <= lh[0]:
                    bricks -= climb
                #if climb is bigger than the smallest in heap, then assign it the bricks and ladder to bigger one
                else:
                    mv = heapq.heappop(lh)   
                    heapq.heappush(lh, climb)
                    bricks -= mv
            # if we run out bricks, we know that we cant move further. 
            if bricks < 0:
                return i
            
        
        return len(heights) - 1
                    
            