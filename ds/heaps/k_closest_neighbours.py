from typing import List 
import heapq
import math

#solution using maxHeap
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    
        def dist(x, y):
            return math.sqrt(x*x + y*y) #can be done without taking the root also.
        
        dHeap = []
        for a, b in points:
            dHeap.append([-1 * dist(a, b), a, b]) #didn't know we can pass a list into a heap, super cool!
    
        heapq.heapify(dHeap)
        
        while(len(dHeap)) > k:
            heapq.heappop(dHeap)
        
        res = []
        for i in range(k):
            res.append([dHeap[i][1], dHeap[i][2]])
        
        return res

#neetcode solution
class Sol:
    def kClosestt(self, points: List[List[int]], k: int) -> List[List[int]]:

        dHeap = []
        for a, b in points:
            dHeap.append([a*a + b*b, a, b])
        
        heapq.heapify(dHeap)
        res = []

        while k > 0:
            _, a, b = heapq.heappop(dHeap)
            res.append([a, b])
            k -= 1
        
        return res

