"""
Time - O(N)
Space - O(N)
23 mins
"""
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        msf = 10e6
        from collections import defaultdict
        hm = defaultdict(list)

        for i, c in enumerate(cards):
            if c in hm:
                msf = min(msf, i - hm[c][-1] + 1)
                hm[c].append(i)
            hm[c].append(i)
        
        counts = sum([len(v) for v in hm.values()])

        return msf if counts > len(cards) else -1

