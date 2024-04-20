import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l = r = 0
        res = []

        while r < len(nums):
            
            # maintain monotonic decreasing queue
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # shrink left
            if l > q[0]:
                q.popleft()
            
            # start adding once size is k 
            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res