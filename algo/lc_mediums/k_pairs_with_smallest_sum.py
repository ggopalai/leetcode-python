class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        visited = set()
        m, n = len(nums1), len(nums2)
        mh = [((nums1[0] + nums2[0]), 0, 0)]
        res = []

        while k and mh:
            s, l, r = heappop(mh)
            res.append([nums1[l], nums2[r]]) 

            if l + 1 < m and (l + 1, r) not in visited:
                heappush(mh, ((nums1[l + 1] + nums2[r]), l + 1, r))
                visited.add((l + 1, r))
            
            if r + 1 < n and (l, r + 1) not in visited:
                heappush(mh, ((nums1[l] + nums2[r + 1]), l, r + 1))
                visited.add((l, r + 1))
            
            k -= 1
        
        return res


     
        
        

        
