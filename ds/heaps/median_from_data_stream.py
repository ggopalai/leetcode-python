# 1. Brute Force - 18/21 passed. 
class MedianFinder:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2:
            return float(self.nums[n // 2])
        else:
            return ((self.nums[n // 2 - 1]) + (self.nums[n // 2])) / 2

# 2. Using 2 heaps 
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        
        #handle sorting case
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        
        #handle uneven length cases
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, heapq.heappop(self.large) * -1)
            

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return (-1 * self.small[0])
        elif len(self.large) > len(self.small):
            return (self.large[0])
        else:
            return ((self.small[0] * -1) + self.large[0]) / 2 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()