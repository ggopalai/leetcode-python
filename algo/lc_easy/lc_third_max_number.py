class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        
        if len(s) < 3:
            return max(s)
        
        l = list(s)
        l.sort() #O(nlogn)
        
        return l[-3]

# follow up - linear solution?
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        
        if len(s) < 3:
            return max(s)
        
        l = [-i for i in s] #max-heap
        
        heapq.heapify(l) #O(n)
        for i in range(2):
            heapq.heappop(l)
        
        return l[0] * -1
        