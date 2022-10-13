import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        mh = nums
        heapq.heapify(mh)
        while len(mh) > k:
            heapq.heappop(mh)
        
        return mh[0]
            