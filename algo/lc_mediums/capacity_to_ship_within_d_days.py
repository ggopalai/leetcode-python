class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(cap):
            d, cur, i = 1, 0, 0
            while i < len(weights):
                cur += weights[i]
                if cur > cap:
                    d += 1
                    cur = weights[i]
                i += 1
            
            return d <= days
        
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if not canShip(mid):
                l = mid + 1
            else:
                if canShip(mid) and not canShip(mid - 1):
                    return mid
                r = mid
        return l